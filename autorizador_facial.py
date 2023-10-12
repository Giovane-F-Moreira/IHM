import face_recognition
import json

ARQUIVO_AUTORIZACOES = "/media/gio/Arquivos_M2/Workspace/IHM/autorizacoes.json"

cache_de_imagens = {}

def configurar():
    autorizados, suspeitos = [], []

    with open(ARQUIVO_AUTORIZACOES, "r") as arquivo:
        autorizacoes = json.load(arquivo)
        if autorizacoes:
            autorizados = autorizacoes["autorizados"]
            suspeitos = autorizacoes["suspeitos"]

    for contador, autorizado in enumerate(autorizados):
        print(f"codificando características faciais de {contador} autorizados")

        foto = face_recognition.load_image_file(autorizado["foto"])
        autorizado["caracteristicas_faciais"] = face_recognition.face_encodings(foto)[0]

    for contador, suspeito in enumerate(suspeitos):
        print(f"codificando características faciais de {contador} suspeitos")

        foto = face_recognition.load_image_file(suspeito["foto"])
        suspeito["caracteristicas_faciais"] = face_recognition.face_encodings(foto)[0]

    return autorizados, suspeitos


def processar_caracteristicas_de_visitantes(foto_visitantes):
    caracteristicas = None

    if foto_visitantes in cache_de_imagens:
        caracteristicas = cache_de_imagens[foto_visitantes]
    else:
        foto = face_recognition.load_image_file(foto_visitantes)
        caracteristicas = face_recognition.face_encodings(foto)

        cache_de_imagens[foto_visitantes] = caracteristicas

    return caracteristicas

def autorizar(autorizados, visitantes):
    acessos_permitidos = []

    caracteristicas_dos_visitantes = processar_caracteristicas_de_visitantes(visitantes)

    # 1. percorrer toda a lista de pessoas autorizadas
    for autorizado in autorizados:
        # 2. testar se a foto da pessoa autorizada está entre os visitantes
        acesso_permitido = True in face_recognition.compare_faces(
            caracteristicas_dos_visitantes, autorizado["caracteristicas_faciais"])
        # 3. se a foto for reconhecida, permitir o acesso e retornar as informacoes de nome e biografia
        if acesso_permitido:
            acessos_permitidos.append(autorizado)

    return len(acessos_permitidos) > 0, acessos_permitidos


def detectar_suspeitos(suspeitos, visitantes):
    suspeitos_detectados = []

    caracteristicas_dos_visitantes = processar_caracteristicas_de_visitantes(visitantes)

    # 1. percorrer toda a lista de pessoas autorizadas
    for suspeito in suspeitos:
        # 2. testar se a foto da pessoa suspeita está entre os visitantes
        suspeito_detectado = True in face_recognition.compare_faces(
            caracteristicas_dos_visitantes, suspeito["caracteristicas_faciais"])
        # 3. se a foto for reconhecida, avisar que suspeito foi reconhecido
        if suspeito_detectado:
            suspeitos_detectados.append(suspeito)

    return len(suspeitos_detectados) > 0, suspeitos_detectados


if __name__ == '__main__':
    autorizados, suspeitos = configurar()

    capturas = ["/media/gio/Arquivos_M2/Workspace/IHM/faces/autorizados1.jpg",
                "/media/gio/Arquivos_M2/Workspace/IHM/faces/autorizados2.jpg",
                "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos1.jpg",
                "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos2.jpg",
                ]
    for captura in capturas:
        print(f"processando captura: {captura}")

        existem_permissoes, acessos_permitidos = autorizar(
            autorizados, captura)
        if existem_permissoes:
            for permissao in acessos_permitidos:
                print(f"permitir acesso para: {permissao['nome']}")
        else:
            print(f"nenhuma pessoa permitida")

        existem_suspeitos, suspeitos_detectados = detectar_suspeitos(
            suspeitos, captura)
        if existem_suspeitos:
            for suspeito in suspeitos_detectados:
                print(f"detectado um suspeito: {suspeito['nome']}")
        else:
            print(f"nenhum suspeito detectado")
