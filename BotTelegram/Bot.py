from telebot import TeleBot
import Classes
import pyodbc
#########################################################################
""" Conexão do banco de dados """

conn = pyodbc.connect(Driver ='SQL Server',Server = 'DESKTOP-2RPK1J7',Database = 'Base_bot')

print("Deu certo! Estamos conectado")
cursor = conn.cursor()
##########################################################################

api_key = "5049818563:AAGifz29ZNs_bLV9eqTGA58I2qAqrQuvCdI"
bot = TeleBot(api_key)
user_dict= {}


def Validar_entrada_string(texto):
    if not texto.isstring():
        print('digite um valor válido para o cadastro!!')
        return
def validar_entrada_números(cpf):
    if not cpf.isdigit():
        print('Digite um cpf válido')
        return
@bot.message_handler(commands= ["1"])
def login(message):
    try:
        bot.send_message(message.chatid,"Insira seu email cadastrado em nosso sistema:")
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands= ["2"])
def cadastro_usuario(message):
    bot.reply_to(message,"Por favor digite o seu nome")
    bot.register_next_step_handler(message,cadastro_nome)

def cadastro_nome(message):
    try:
        chatid= message.chat.id# recebe o id do chat do usuário
        chat_id= int(chatid)
        nome = message.text
        user = Classes.Usuario(nome)
        user_dict[chat_id] = user
        print(nome)
        msg = bot.reply_to(message.chat.id, "Insira um Email válido para o cadastro:")
        bot.register_next_step_handler(msg,cadastro_email)
    except Exception as e:
        bot.reply_to(message, str(e))


def cadastro_email(message):
    try:
        chatid = message.chat.id  # recebe o id do chat do usuário
        chat_id = int(chatid)
        email = message.text
        user = Classes.Usuario(email)
        user_dict[chat_id] = user
        print(email)
        bot.reply_to(message.chat.id, "Insira um CPF válido para o cadastro:")
        bot.register_next_step_handler(message, cadastro_cpf)
    except Exception as e:
        bot.reply_to(message, str(e))


def cadastro_cpf(message):
    try:
        chatid = message.chat.id  # recebe o id do chat do usuário
        chat_id = int(chatid)
        cpf = message
        user = Classes.Usuario(cpf)
        user_dict[chat_id] = user
        print(cpf)
        bot.reply_to(message.chat.id, "Agradecemos a preferência")
        insert_user ="INSERTINTO  Usuario(Nome, cpf, email) VALUES(%s,%s,%s)"

        return

    except Exception as e:
        bot.reply_to(message, str(e))


@bot.message_handler(commands= ["3"])
def consulta(message):
    text = """
    /Agendar consulta
    /Ver Consultas
    """


@bot.message_handler(commands=["/Agendar"])
def agendar_consulta(message):
    try:
        chat_id=  message.chatid
    except Exception as e:
        bot.reply_to(message, str(e))


@bot.message_handler(commands=["/Ver Consultas"])
def verificar_consulta(message):
    try:
        chat_id=  message.chatid
    except Exception as e:
        bot.reply_to(message, str(e))


@bot.message_handler(commands= ["4"])
def planos(message):
    text = """
        Escolha uma opção de Plano:
        /Básico
        /Intermediário
        /Premium
        """


    @bot.message_handler(commands=["Básico"])
    def basic(message):
        bot.send_message(message.chat.id, "Inclue consultas online 1 vez por semana 129,90/mês")


    @bot.message_handler(commands=["Intermediário"])
    def intermediary(message):
        bot.send_message(message.chat.id, "Inclue ate 3 consultas online e video chamadas por semana 200,00/mês")


    @bot.message_handler(commands=["Premium"])
    def premium(message):
        bot.send_message(message.chat.id, "1 consulta diária, com acompanhamento médico presencial e online 350,00/mês")



@bot.message_handler(commands= ["5"])
def contato(message):
    bot.send_message(message.chat.id,'Em caso de dúvidas  ou buscando um atendimento de um humano, ligue no númeor : 11 4103-9587')


def verifier(message):
    return True


@bot.message_handler(commands= ["start"])
def menu_bot(message):
    print(message)
    text = """
    Seja bem vindo aos serviços de You Never Walk Alone, por favor seleciona uma das opções abaixo:
    /1 - Login
    /2 - Cadastro
    /3 - Agendar consulta
    /4 - Conhecer planos
    /5 - Número de contato"""
    bot.reply_to(message, text)


bot.polling()