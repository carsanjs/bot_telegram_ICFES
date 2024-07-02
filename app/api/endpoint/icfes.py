from fastapi import APIRouter
import requests

icfes_router = APIRouter()


@icfes_router.get("/icfesMayor2021")
async def first_request(doc, reg, td):
    data = {
        "tipoDocumento": td.upper(),
        "numeroDocumento": doc,
        "fechaNacimiento": None,
        "identificacionUnica": reg.upper(),
    }
    try:
        #✅Pruebas Saber 11 realizadas a partir del 2021: https://resultadossaber11.icfes.edu.co/login.
        res = requests.post(
            "https://resultadosbackendoci.icfes.edu.co/api/segurity/autenticacionResultados",
            json=data,
        ).json()
        print("response data -->", res)
        print("request")
        try:
            fechaNacimiento = (
                res.get("dataAutenticacion")[0]
                .get("datosParametros")
                .get("fechaNacimiento")
            )
        except:
            return "bad"

        token = res.get("token")
        res = requests.get(url=f'https://resultadosbackend.icfes.gov.co/api/datos-basicos/datosBasicosRespuesta?examen=SB11&identificacionUnica', headers={'Authorization': token}).json()
       
        period = res.get('periodoResultado')
        name = res.get('camposDatosBasicos')[0].get('valorDatoBasico')
        school = res.get('camposDatosBasicos')[7].get('valorDatoBasico')
        
        res = requests.get(url=f'https://resultadosbackend.icfes.gov.co/api/resultados/datosReporteGeneral?identificacionUnica={reg.upper()}&examen=SB11&periodoAnioExamen={period}',  headers={'Authorization': token}).json()
        resultado = res.get('resultadosGenerales').get('puntajeGlobal')
        perc = res.get('resultadosGenerales').get('percentilNacional')
        print(f'Nombre: {name}, Escuela: {school}, Resultado: {resultado}, Percentil Nacional: {perc}%')
    except:
        print("error")
        return "bad"
    
    final_message = f'''Oye, {name} obtuviste <{resultado}>. Nacido el {fechaNacimiento}. 
    Colegio: {school}.
    Tu puntaje está por encima del {perc}% a nivel nacional.
    '''

    return final_message




@icfes_router.get("/icfesMenor2021")
async def second_request(doc, reg, td):
    data = {
        "tipoDocumento": td.upper(),
        "numeroDocumento": doc,
        "numeroRegistro": None,
        "fechaNacimiento": None,
        "identificacionUnica": reg.upper(),
    }
    try:
        # ✅ Pruebas Saber 11 anteriores al 2021: https://resultadoshistoricos.icfes.edu.co/login 
        res = requests.post('https://resultadosbackendoci.icfes.edu.co/api/seguritypro/resultadosGeneral/unificacionResultados/consultar',
            json=data,
        ).json()
        print("response data -->", res)
        print("request")
        try:
            fechaNacimiento = (
                res.get("dataAutenticacion")[0]
                .get("datosParametros")
                .get("fechaNacimiento")
            )
        except:
            return "bad"

        token = res.get("token")
        res = requests.get("", headers={"Authorization": token}).json()

    except:
        print("error")
        return "bad"



def main(reg,doc,td):

  response = first_request(reg=reg, doc=doc, td=td)

  if response != 'bad':
    return response, False

  else:
    return 'bad', False