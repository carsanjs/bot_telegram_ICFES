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
        res = requests.get("", headers={"Authorization": token}).json()

    except:
        print("error")
        return "bad"
    




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
