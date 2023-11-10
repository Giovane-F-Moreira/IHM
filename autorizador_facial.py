import face_recognition
import json
import random
import colored

DATABASE = "/media/gio/Arquivos_M2/Workspace/IHM/database.json"

EVENTUALIDADE_FUGA = 80
EVENTUALIDADE_TENTATIVA_FUGA = 80
EVENTUALIDADE_DESENTENDIMENTO = 60
EVENTUALIDADE_DESENTENDIMENTO_VERBAL = 70
EVENTUALIDADE_DESENTENDIMENTO_FISICO = 60
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

def obter_nome_autorizado_por_id(arquivo_json, id_procurado):
    try:
        with open(arquivo_json, 'r') as arquivo:
            data = json.load(arquivo)
            autorizado = data['autorizados']
            for autorizado in autorizado:
                if autorizado['id'] == id_procurado:
                    print(f"Nome: {autorizado.get('nome', None)}")
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
    id_autorizado = int(random.uniform(1, 5))            
    nome = obter_nome_autorizado_por_id(DATABASE, id_autorizado)
    return id_autorizado, nome
    
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
   
def set_pena(id, pena):
    with open('database.json', 'r') as file:
        data = json.load(file)
    
        print(f"Pena: {data['suspeitos'][id-1]['pena']}")
        data['suspeitos'][id-1]['pena'] += pena
        print(f"pena aumentada: {data['suspeitos'][id-1]['pena']}")
        
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)  # indent=4 para uma formatação mais legível

    print("-")
    ...   

def eventualidade_fuga(tentativa_de_fuga, fuga):
    _, suspeitos = ler_database()
    
    eventos = []
    vai_tentar_fugir = False

    id_detento, nome_detento, foto_detento = sortear_detento()
    print(f"DETENTO: {id_detento} {nome_detento} {foto_detento}") 
    detento = None
        
    # EVENTUALIDADE DE TENTATIVA DE FUGA OU FUGA
    tentar_fugir = int(random.uniform(0, 100))
    print(f'{tentar_fugir}%')
    if tentar_fugir <= tentativa_de_fuga:
        
        detectou = detectar_suspeitos(suspeitos, obter_foto_suspeito_por_id(DATABASE, id_detento))
        
        vai_tentar_fugir = True
        eventos.append(vai_tentar_fugir)
        print(colored.fg('black'), colored.bg('yellow'),f"{nome_detento} vai tentar fugir !", colored.attr('reset'))
        
        fugir = int(random.uniform(0, 100))
        
        if fugir <= fuga:
            chance_ser_pego = int(random.uniform(0, 100))           
            print(f'criminoso que está fugindo: {nome_detento}')
            print(f'Chance_ser_pego de ser pego: {chance_ser_pego}')
            
            
            if chance_ser_pego <= PRENDER_FUGITIVO:
    
                if detectou: 
                    fugiu=False               
                    eventos.append(fugiu)
                    print(colored.fg('black'), colored.bg('green'),f'{nome_detento} foi pego DURANTE A FUGA', colored.attr('reset'))
                else:
                    fugiu=False
                    eventos.append(fugiu) 
                    print(colored.fg('black'), colored.bg('yellow'),f'Criminoso foi pego, porém não está cadastrado ou não foi identificado', colored.attr('reset'))
            else:
                fugiu = True
                eventos.append(fugiu)
                print(colored.fg('black'), colored.bg('red'),f'{nome_detento} FUGIU !', colored.attr('reset'), colored.attr('reset'))                
        else:
            fugiu = False
            print(colored.fg('black'), colored.bg('green'),f'{nome_detento} foi pego na TENTATIVA de fugir', colored.attr('reset'))
            eventos.append(fugiu)
            
    else:
        vai_tentar_fugir = False
        fugiu = False
        eventos.append(vai_tentar_fugir)
        eventos.append(fugiu) 
        detento = None
        print(colored.fg('black'), colored.bg('blue'),f'Não houve eventualidades', colored.attr('reset'))  
        
    print(eventos)
    return 
    
def patio(lista_presidiarios):
    eventualidade_fuga(EVENTUALIDADE_TENTATIVA_FUGA, EVENTUALIDADE_FUGA)
    
    qtd_detentos = len(lista_presidiarios)
    
    
    print(eventualidade_desentendimento(70, 60))

def refeitorio(lista_presidiarios, autorizados): 
    ...
    
def celas(lista_presidiarios, autorizados):
    ...

def enfermaria(lista_presidiarios, autorizados):
    ...


if __name__ == '__main__':
    
     patio(lista_detentos(DATABASE))
     
      
    # autorizados, suspeitos = ler_database()

    # capturas = ["/media/gio/Arquivos_M2/Workspace/IHM/faces/autorizados1.jpg",
    #             "/media/gio/Arquivos_M2/Workspace/IHM/faces/autorizados22.jpg",
    #             "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos1.jpg",
    #             "/media/gio/Arquivos_M2/Workspace/IHM/faces/suspeitos2.jpg",
    #             ]
    # for captura in capturas:
    #     print(f"processando captura: {captura}")

    #     existem_permissoes, acessos_permitidos = autorizar(
    #         autorizados, captura)
    #     if existem_permissoes:
    #         for permissao in acessos_permitidos:
    #             print(colored.fg('black'), colored.bg('green'),f"permitir acesso para: {permissao['nome']}", colored.attr('reset'))
    #     else:
    #         print(colored.fg('black'), colored.bg('yellow'),f"nenhuma pessoa permitida", colored.attr('reset'))

    #     existem_suspeitos, suspeitos_detectados = detectar_suspeitos(
    #         suspeitos, captura)
    #     if existem_suspeitos:
    #         for suspeito in suspeitos_detectados:
    #             print(colored.fg('black'), colored.bg('red'),f"detectado um suspeito: {suspeito['nome']}", colored.attr('reset'))
    #     else:
    #         print(colored.fg('black'), colored.bg('white'),f"nenhum suspeito detectado", colored.attr('reset'))
            
    # eventualidade(EVENTUALIDADE_TENTATIVA_FUGA, EVENTUALIDADE_FUGA, EVENTUALIDADE_DESENTENDIMENTO)