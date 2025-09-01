from telegram.ext import ApplicationBuilder, Application, ConversationHandler, CommandHandler


#TELEGRAM
class TelegramBotCommand:

    def __init__(
        self,
        telegram_api_token: str,
        id_auths: list[str]
    ):
        self.token = telegram_api_token
        self.id_auths = id_auths
        self.conversation_handler: ConversationHandler = None
        self.application: Application = None
        self.application = ApplicationBuilder().token(self.token).build()

    def bind(self):
        # self.application = ApplicationBuilder().token(self.token).build()

        # # Registrar el comando /start directamente
        # # self.application.add_handler(CommandHandler("start", self.start))

        # # Registrar el ConversationHandler para el resto del flujo
        # self.application.add_handler(self.converstaion_handler)

        self.application.run_polling()




from functools import wraps

def save_state_command_bot(method):
    @wraps(method)
    def wrapper(self, update, context, *args, **kwargs):
        # Ejecutamos el método original
        resultado = method(self, update, context, *args, **kwargs)

        # Guardamos estado en Redis
        user_id = update.effective_user.id
        estado_usuario = context.user_data.copy()
        if self.base64image:
            estado_usuario['base64image'] = self.base64image
        self.keyvalue_db.set(f'state:{user_id}', estado_usuario)

        return resultado
    return wrapper