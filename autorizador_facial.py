import face_recognition
import json
import random
import colored
import simpy
 
DATABASE = "/media/gio/Arquivos_M2/Workspace/IHM/database.json"

EVENTUALIDADE_FUGA = 15
EVENTUALIDADE_TENTATIVA_FUGA = 30
EVENTUALIDADE_DESENTENDIMENTO = 60
EVENTUALIDADE_DESENTENDIMENTO_VERBAL = 45
EVENTUALIDADE_DESENTENDIMENTO_FISICO = 30
EVENTUALIDADE_PEGO_EM_OUTRA_ALA = 65

TEMPO_CHECAGEM_PAVILHAO_CELAS = 10
TEMPO_PATIO = 180
TEMPO_REFEITORIO = 90

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

def autorizar(autorizados, capturas):
    acessos_permitidos = []

    caracteristicas_das_capturas = processar_caracteristicas_faciais(capturas)

    # 1. percorrer toda a lista de pessoas autorizadas
    for autorizado in autorizados:
        # 2. testar se a foto da pessoa autorizada está entre as capturas de imagem
        acesso_permitido = True in face_recognition.compare_faces(
            caracteristicas_das_capturas, autorizado["caracteristicas_faciais"])
        # 3. se a foto for reconhecida, permitir o acesso e retornar as informacoes de nome e biografia
        if acesso_permitido:
            acessos_permitidos.append(autorizado)

    return len(acessos_permitidos) > 0, acessos_permitidos

def identificar_detento(suspeitos):
    
    detentos_identificados = []
    caracteristicas_faciais_processadas = []
    
    capturas = [
        "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos1.jpg",
        "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos2.jpg"
        ]
    
    for captura in capturas:

        caracteristicas_faciais_processadas = processar_caracteristicas_faciais(captura)

        # 1. percorrer toda a lista de pessoas autorizadas
        for suspeito in suspeitos:
            # 2. testar se a foto da pessoa autorizada está entre os visitantes
            detento = True in face_recognition.compare_faces(
                caracteristicas_faciais_processadas, suspeito["caracteristicas_faciais"])
            # 3. se a foto for reconhecida, permitir o acesso e retornar as informacoes de nome e biografia
            if detento:
                print(colored.fg('black'), colored.bg('white'),f"{suspeito['nome']} identificado!", colored.attr('reset'))
                try:
                    detentos_identificados.index(suspeito)
                except:
                    detentos_identificados.append(suspeito)

    return len(detentos_identificados) > 0, detentos_identificados

def lista_detentos(arquivo_json):
    detentos = []
    
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['detento'] == 'sim':
                    detentos.append(suspeito['nome'])
            return detentos
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None
    
    
    return detentos

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
def sair_penitenciaria(arquivo_json, nome):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['nome'] == nome:
                    id = obter_id_suspeito_por_nome(arquivo_json, nome)
                    set_status_detento(id, 'nao')
                    print(colored.fg('black'), colored.bg('white'),f'{nome} acaba de sair da penitenciaria por cumprir sua sentença!', colored.attr('reset'))
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None   
    
def buscar_crimonoso_id(arquivo_json, id):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            for categoria in data:
                for item in data[categoria]:
                    if item['id'] == id:
                        return item.get('foto', None)
        return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None

def obter_id_suspeito_por_nome(arquivo_json, nome):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['nome'] == nome:
                    return suspeito.get('id', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None  

def obter_foto_suspeito_por_nome(arquivo_json, nome):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['nome'] == nome:
                    return suspeito.get('foto', None)
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
                    return suspeito.get('nome', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None    

def obter_nome_autorizado_por_id(arquivo_json, id_procurado):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            autorizado = data['autorizados']
            for autorizado in autorizado:
                if autorizado['id'] == id_procurado:
                    return autorizado.get('nome', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None  

def sortear_detento():
    id_crimonoso = int(random.uniform(1, 5))            
    foto = obter_foto_suspeito_por_id(DATABASE, id_crimonoso)
    nome = obter_nome_suspeito_por_id(DATABASE, id_crimonoso)
    return id_crimonoso, nome, foto

def sortear_autorizado():
    id_autorizado = int(random.uniform(1, 4))            
    nome = obter_nome_autorizado_por_id(DATABASE, id_autorizado)
    return id_autorizado, nome
    
def eventualidade_pego_em_outra_ala(local_atual, chance_acontecer):
    
    numero_aleatorio = int(random.uniform(0, 100))
    
    if numero_aleatorio <= chance_acontecer:
        locais = ['patio','pavilhao de celas','refeitorio']
    
        index = (int(random.uniform(1, 4))-1)
        
        while locais[index] == local_atual:
            index = (int(random.uniform(1, 4))-1)
            
        id, nome, _ = sortear_detento()
        set_pena(id, 15)
        print(colored.fg('black'), colored.bg('red'),f'{nome} foi pego no {locais[index]} fora do horario permitido e teve sua pena aumentada em 15 Dias', colored.attr('reset'))
        
    else:
        print(colored.fg('black'), colored.bg('white'),f'Nenhuma eventualidade ocorrida', colored.attr('reset'))
    
def eventualidade_desentendimento(probabilidade_desentendimento_verbal, probabilidade_desentendimento_fisico):
       
    id, nome_detento, _ = sortear_detento()

    _, nome_autorizado = sortear_autorizado()
    
    detento = None
    
    #SORTEIA O TIPO DE DESENTENDIMENTO
    tipo_desentendimento = int(random.uniform(1, 4)) 
    
    if tipo_desentendimento == 1:
    
        propablidade_ocorrer = int(random.uniform(1, 100))
        
        if propablidade_ocorrer <= probabilidade_desentendimento_verbal:
            set_pena(id,90)
            detento = nome_detento
            print(colored.fg('black'), colored.bg('red'),f'{nome_detento} AMEAÇOU {nome_autorizado} e teve sua pena aumentada em 90 dias', colored.attr('reset'))
        else:
            set_pena(id,7)
            detento = nome_detento
            print(colored.fg('black'), colored.bg('red'),f'{nome_detento} ofendeu VERBALMENTE {nome_autorizado} e teve sua pena aumentada em 7 dias', colored.attr('reset'))
    else:
        
        if tipo_desentendimento == 2:
            propablidade_ocorrer2 = int(random.uniform(1, 100))
            if propablidade_ocorrer2 <= probabilidade_desentendimento_fisico:  
                set_pena(id,120)
                detento = nome_detento
                print(colored.fg('black'), colored.bg('red'),f'{nome_detento} tentou AGREDIR {nome_autorizado} e teve sua pena aumentada em 120 dias', colored.attr('reset')) 
            else:
                detento = nome_detento
                print(colored.fg('black'), colored.bg('red'),f'{nome_detento} ofendeu VERBALMENTE {nome_autorizado} e teve sua pena aumentada em 7 dias', colored.attr('reset'))     
        else:
            detento = None
            print(colored.fg('black'), colored.bg('yellow'),f'Não houve nenhuma ocorrencia', colored.attr('reset'))     

    return detento
   
def get_pena(arquivo_json, id):   
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['id'] == id:
                    return suspeito.get('pena', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None  
    
def set_pena(id, pena):
    with open('database.json', 'r') as file:
        data = json.load(file)
    
        print(f"Pena: {data['suspeitos'][id-1]['pena']}")
        data['suspeitos'][id-1]['pena'] += pena
        print(f"Pena alterada: {data['suspeitos'][id-1]['pena']}")
        
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)  # indent=4 para uma formatação mais legível
 
def get_status_detento(arquivo_json, id):   
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            suspeitos = data['suspeitos']
            for suspeito in suspeitos:
                if suspeito['id'] == id:
                    return suspeito.get('detento', None)
            return None
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return None   
 
def set_status_detento(id, status):
    with open('database.json', 'r') as file:
        data = json.load(file)
    
        data['suspeitos'][id-1]['detento'] = status
        print(f"Status modificado:")
        
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)  # indent=4 para uma formatação mais legível
    
def verificar_tempo_pena(env, lista_detentos):
    
    print(f'--------------- Tempo ATUAL: {env.now} -------------------')
    if env.now != 0 and env.now % 1440 == 0:
        for i in lista_detentos:
            print(f'Passou um dia ')  
            print(f'{obter_nome_suspeito_por_id(DATABASE, (lista_detentos.index(i)+1))} tinha que cumprir uma pena de: {get_pena(DATABASE, lista_detentos.index(i)+1)} dias')
            set_pena(lista_detentos.index(i)+1,-1)
            print(f'Sentença atual de {obter_nome_suspeito_por_id(DATABASE, (lista_detentos.index(i)+1))} é: {get_pena(DATABASE, lista_detentos.index(i)+1)} dias')
            pena = get_pena(DATABASE, (i+1))
            if pena == 0:
                pass
            else:
                pass
        print(f'Após passar 24 horas, todos os detentos tiveram a pena reduzida em 1 dia')
    else:  
        pass 
    
def eventualidade_fuga(tentativa_de_fuga, fuga):
    _, suspeitos = ler_database()
    
    eventos = []
    vai_tentar_fugir = False

    id_detento, nome_detento, foto_detento = sortear_detento() 
    detento = None
        
    # EVENTUALIDADE DE TENTATIVA DE FUGA OU FUGA
    tentar_fugir = int(random.uniform(0, 100))

    if tentar_fugir <= tentativa_de_fuga:
        
        detectou = detectar_suspeitos(suspeitos, obter_foto_suspeito_por_id(DATABASE, id_detento))
        
        vai_tentar_fugir = True
        eventos.append(vai_tentar_fugir)
        print(colored.fg('black'), colored.bg('yellow'),f"{nome_detento} vai tentar fugir !", colored.attr('reset'))
        
        fugir = int(random.uniform(0, 100))
        
        if fugir <= fuga:
            set_pena(id_detento, 240)
            print(f'Criminoso que está fugindo: {nome_detento}')
            print(colored.fg('black'), colored.bg('red'),f'{nome_detento} FUGIU e teve a pena aumentada em 480 Dias', colored.attr('reset'))
            detento = nome_detento
            return  detento
                
        else:
            
            #reconhecimento facial 
            set_pena(id_detento, 240)
            fugiu = False
            print(colored.fg('black'), colored.bg('green'),f'{nome_detento} foi pego na TENTATIVA de fuga e teve a pena aumentada em 240 Dias', colored.attr('reset'))
            eventos.append(fugiu)
            
    else:
        vai_tentar_fugir = False
        fugiu = False
        eventos.append(vai_tentar_fugir)
        eventos.append(fugiu) 
        detento = None
        print(colored.fg('black'), colored.bg('blue'),f'Não houve eventualidades', colored.attr('reset'))  
    return detento
    
def patio(env, temp, lista_detentos):
    
    print(colored.fg('black'), colored.bg('blue'),f'Os Detentos estão no patio ! TEMPO ATUAL: {env.now} Minutos', colored.attr('reset'))
    fuga = False
    while True:
        
        _, detectados = identificar_detento(lista_detentos)
        if len(lista_detentos) == len(detectados) and fuga == False:
            print(colored.fg('black'), colored.bg('white'),f'Quantidade de detentos conferido', colored.attr('reset'))
       
        eventualidade_pego_em_outra_ala('patio', EVENTUALIDADE_PEGO_EM_OUTRA_ALA)
        eventualidade_desentendimento(EVENTUALIDADE_DESENTENDIMENTO_VERBAL, EVENTUALIDADE_DESENTENDIMENTO_FISICO)
        evento_ocorrido = eventualidade_fuga(EVENTUALIDADE_TENTATIVA_FUGA, EVENTUALIDADE_FUGA)
        
        if evento_ocorrido == None:
            fuga = False
        else:
            fuga = True
            
        print(colored.fg('black'), colored.bg('white'),f'Tempo Patio: {env.now}', colored.attr('reset'))
        verificar_tempo_pena(env, lista_detentos)
        yield env.timeout(temp)

def refeitorio(env, temp, lista_detentos): 

    print(colored.fg('black'), colored.bg('blue'),f'Os detentos ir\u00e3o passar pelo reconhecimento facial e seguir\u00e3o para fazer a refeição  TEMPO ATUAL: {env.now} Minutos', colored.attr('reset'))
  
    while True:  
        
        _, detectados = identificar_detento(suspeitos)
        if len(lista_detentos) == len(detectados):
            print(colored.fg('black'), colored.bg('white'),f'Quantidade de detentos conferido', colored.attr('reset'))
       
        eventualidade_pego_em_outra_ala('refeitorio', EVENTUALIDADE_PEGO_EM_OUTRA_ALA)
        eventualidade_desentendimento(EVENTUALIDADE_DESENTENDIMENTO_VERBAL, EVENTUALIDADE_DESENTENDIMENTO_FISICO)
        print(colored.fg('black'), colored.bg('white'),f'Tempo: {env.now}', colored.attr('reset'))
        verificar_tempo_pena(env, lista_detentos)
        yield env.timeout(temp)
    
def pavilhao_celas(env, temp, lista_detentos, autorizados, suspeitos):           

    print(colored.fg('black'), colored.bg('blue'),f'Os Detentos estão nos pavilhoes onde estao as celas! TEMPO ATUAL: {env.now}', colored.attr('reset'))
  
    while True:  
        
        
        _, detectados = identificar_detento(suspeitos)
        
        if len(lista_detentos) == len(detectados):
            print(colored.fg('black'), colored.bg('white'),f'Lista de detentos conferida', colored.attr('reset'))

        eventualidade_pego_em_outra_ala('pavilhao de celas', EVENTUALIDADE_PEGO_EM_OUTRA_ALA)
        eventualidade_desentendimento(EVENTUALIDADE_DESENTENDIMENTO_VERBAL,EVENTUALIDADE_DESENTENDIMENTO_FISICO)
        eventualidade_fuga(EVENTUALIDADE_TENTATIVA_FUGA, EVENTUALIDADE_FUGA)
        print(colored.fg('black'), colored.bg('white'),f'Tempo: {env.now}', colored.attr('reset'))
        verificar_tempo_pena(env, lista_detentos)
        yield env.timeout(temp)

if __name__ == '__main__':

    lista_presidiarios = lista_detentos(DATABASE)
 
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
                print(colored.fg('black'), colored.bg('green'),f"Acesso permitido para: {permissao['nome']}", colored.attr('reset'))
        else:
            print(colored.fg('black'), colored.bg('yellow'),f"Nenhuma pessoa permitida", colored.attr('reset'))

        existem_suspeitos, suspeitos_detectados = detectar_suspeitos(
            suspeitos, captura)
        if existem_suspeitos:
            for suspeito in suspeitos_detectados:
                print(colored.fg('black'), colored.bg('red'),f"{suspeito['nome']} é considerado um suspeito!", colored.attr('reset'))
        else:
            print(colored.fg('black'), colored.bg('white'),f"Nenhum suspeito detectado", colored.attr('reset'))
    
    env = simpy.Environment()
    
    env.process(pavilhao_celas(env, TEMPO_CHECAGEM_PAVILHAO_CELAS, lista_presidiarios, autorizados, suspeitos))
    print(colored.fg('black'), colored.bg('white'),f'Tempo pavilh\xe3o: {env.now}', colored.attr('reset'))
    
    env.process(patio(env, TEMPO_PATIO, suspeitos))
    print(colored.fg('black'), colored.bg('white'),f'Tempo patio: {env.now}', colored.attr('reset'))
    
    env.process(refeitorio(env, TEMPO_REFEITORIO, lista_presidiarios))
    print(colored.fg('black'), colored.bg('white'),f'Tempo refeitorio: {env.now}', colored.attr('reset'))
    
    env.process(patio(env, TEMPO_PATIO, suspeitos))
    print(colored.fg('black'), colored.bg('white'),f'Tempo patio: {env.now}', colored.attr('reset'))
    
    env.process(pavilhao_celas(env, TEMPO_CHECAGEM_PAVILHAO_CELAS, lista_presidiarios, autorizados, suspeitos))
    print(colored.fg('black'), colored.bg('white'),f'Tempo pavilh\xe3o: {env.now}', colored.attr('reset'))
    
    env.run(until=2000)    