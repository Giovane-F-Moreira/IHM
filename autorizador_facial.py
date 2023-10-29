import face_recognition
import json
import random

DATABASE = "/media/gio/Arquivos_M2/Workspace/IHM/database.json"
EVENTUALIDADE_FUGA = 0.01
DESENTENDIMENTO = 0.20
EVENTUALIDADE_TENTATIVA_FUGA = 0.02 
TEMPO_DIA_MINUTOS = 1440
TEMPO_ANO_MINUTOS = 525_600

cache_de_imagens = {}

# ============== Banco de Dados ==============
def ler_database():
    autorizados, suspeitos = [], []

    with open(DATABASE, "r") as arquivo:
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


# ============== Camera =====================
def processar_caracteristicas_faciais(foto):
    caracteristicas = None

    if foto in cache_de_imagens:
        caracteristicas = cache_de_imagens[foto]
    else:
        processar_foto = face_recognition.load_image_file(foto)
        caracteristicas = face_recognition.face_encodings(processar_foto)

        cache_de_imagens[foto] = caracteristicas

    return caracteristicas

def autorizar(autorizados, visitantes):
    acessos_permitidos = []

    caracteristicas_dos_visitantes = processar_caracteristicas_faciais(visitantes)

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

    caracteristicas_dos_visitantes = processar_caracteristicas_faciais(visitantes)

    # 1. percorrer toda a lista de pessoas autorizadas
    for suspeito in suspeitos:
        # 2. testar se a foto da pessoa suspeita está entre os visitantes
        suspeito_detectado = True in face_recognition.compare_faces(
            caracteristicas_dos_visitantes, suspeito["caracteristicas_faciais"])
        # 3. se a foto for reconhecida, avisar que suspeito foi reconhecido
        if suspeito_detectado:
            suspeitos_detectados.append(suspeito)

    return len(suspeitos_detectados) > 0, suspeitos_detectados


# =============== Simulação ====================
def simular_dia():
    eventualidade()
    celas()
    patio()
    refeitorio()
    patio()
    refeitorio()
    celas()
    ...
    
def entrar_penitenciaria(lista_presidiarios, autorizados):
    ...
    
def sair_penitenciaria(lista_presidiarios, autorizados):
    ...

def eventualidade(fuga, desentendimento, tentativa_de_fuga):
    ...
    
def patio(lista_presidiarios, autorizados):
    ...

def refeitorio(lista_presidiarios, autorizados): 
    ...
    
def celas(lista_presidiarios, autorizados):
    ...

def enfermaria(lista_presidiarios, autorizados):
    ...


if __name__ == '__main__':
    autorizados, suspeitos = ler_database()

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
