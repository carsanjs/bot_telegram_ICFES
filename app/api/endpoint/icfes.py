from fastapi import APIRouter
import requests

icfes_router = APIRouter()


@icfes_router.get("/icfes")
async def first_request(doc, reg, td):
    data = {
        "tipoDocumento": td.upper(),
        "numeroDocumento": doc,
        "fechaNacimiento": None,
        "identificacionUnica": reg.upper(),
    }
    try:
        res = requests.post(
            "https://resultadosbackendoci.icfes.edu.co/api/segurity/autenticacionResultados",
            json=data,
        ).json()
        print("response data -->", res)
        print("request")
        try:
            fechaNacimiento = (
                res.get("datosAutenticacion")[0]
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
