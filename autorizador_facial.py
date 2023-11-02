import face_recognition
import json
import random
import colored

DATABASE = "/media/gio/Arquivos_M2/Workspace/IHM/database.json"
EVENTUALIDADE_FUGA = 80
EVENTUALIDADE_DESENTENDIMENTO = 9
EVENTUALIDADE_TENTATIVA_FUGA = 80
PRENDER_FUGITIVO = 1
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
    
    # celas()
    # patio()
    # refeitorio()
    # patio()
    # refeitorio()
    # celas()
    ...
    
def entrar_penitenciaria(lista_presidiarios, autorizados):
    ...
    
def sair_penitenciaria(lista_presidiarios, autorizados):
    ...
def buscar_crimonoso_id(arquivo_json, id):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            for categoria in data:
                for item in data[categoria]:
                    if item['id'] == id:
                        print(f"Foto: {item.get('foto', None)}")
                        return item.get('foto', None)
        return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None

def obter_foto_suspeito_por_id(arquivo_json, id_procurado):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['id'] == id_procurado:
                    print(f"Foto: {suspeito.get('foto', None)}")
                    return suspeito.get('foto', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None
    
def obter_nome_suspeito_por_id(arquivo_json, id_procurado):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['id'] == id_procurado:
                    print(f"Nome: {suspeito.get('nome', None)}")
                    return suspeito.get('nome', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None    

def eventualidade(tentativa_de_fuga, fuga, desentendimento):
    autorizados, suspeitos = ler_database()
    
    eventos = []
    vai_tentar_fugir = False
    
    tentar_fugir = int(random.uniform(0, 100))
    print(f'{tentar_fugir}%')
    if tentar_fugir <= tentativa_de_fuga:
        crimonoso = int(random.uniform(1, 4))            
        detectou = detectar_suspeitos(suspeitos, obter_foto_suspeito_por_id(DATABASE, crimonoso))
        nome = obter_nome_suspeito_por_id(DATABASE, crimonoso)
        
        vai_tentar_fugir = True
        print(colored.fg('black'), colored.bg('yellow'),f"{nome} vai tentar fugir !", colored.attr('reset'))
        eventos.append(vai_tentar_fugir)
        
        fugir = int(random.uniform(0, 100))
        
        if fugir <= fuga:
            chance_ser_pego = int(random.uniform(0, 100))           
            print(f'criminoso que está fugindo: {crimonoso}')
            print(f'Chance_ser_pego de ser pego: {chance_ser_pego}')
            
            
            if chance_ser_pego <= PRENDER_FUGITIVO:
    
                if detectou: 
                    fugiu=False               
                    eventos.append(fugiu)
                    print(colored.fg('black'), colored.bg('green'),f'{nome} foi pego DURANTE A FUGA', colored.attr('reset'))
                else:
                    fugiu=False
                    eventos.append(fugiu) 
                    print(colored.fg('black'), colored.bg('yellow'),f'Criminoso foi pego, porém não está cadastrado ou não foi identificado', colored.attr('reset'))
            else:
                fugiu = True
                eventos.append(fugiu)
                print(colored.fg('black'), colored.bg('red'),f'{nome} FUGIU !', colored.attr('reset'), colored.attr('reset'))                
        else:
            fugiu = False
            print(colored.fg('black'), colored.bg('green'),f'{nome} foi pego na TENTATIVA de fugir', colored.attr('reset'))
            eventos.append(fugiu)
            
    else:
        vai_tentar_fugir = False
        fugiu = False
        print("vai_tentar_fugir FALSE")
        eventos.append(vai_tentar_fugir)
        eventos.append(fugiu)
        
    print(eventos)
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
                "/media/gio/Arquivos_M2/Workspace/IHM/faces/autorizados22.jpg",
                "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos1.jpg",
                "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos2.jpg",
                ]
    for captura in capturas:
        print(f"processando captura: {captura}")

        existem_permissoes, acessos_permitidos = autorizar(
            autorizados, captura)
        if existem_permissoes:
            for permissao in acessos_permitidos:
                print(colored.fg('black'), colored.bg('green'),f"permitir acesso para: {permissao['nome']}", colored.attr('reset'))
        else:
            print(colored.fg('black'), colored.bg('yellow'),f"nenhuma pessoa permitida", colored.attr('reset'))

        existem_suspeitos, suspeitos_detectados = detectar_suspeitos(
            suspeitos, captura)
        if existem_suspeitos:
            for suspeito in suspeitos_detectados:
                print(colored.fg('black'), colored.bg('red'),f"detectado um suspeito: {suspeito['nome']}", colored.attr('reset'))
        else:
            print(colored.fg('black'), colored.bg('white'),f"nenhum suspeito detectado", colored.attr('reset'))
            
    eventualidade(EVENTUALIDADE_TENTATIVA_FUGA, EVENTUALIDADE_FUGA, EVENTUALIDADE_DESENTENDIMENTO)