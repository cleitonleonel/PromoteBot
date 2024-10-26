from telethon import TelegramClient, events
from telethon.tl.types import InputReplyToMessage
from telethon.tl.functions.messages import SendMessageRequest
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']
session_name = config['Telegram']['session_name']

reply_channel_id = int(config['Channels']['reply_channel_id'])
channel_id = int(config['Channels']['channel_id'])
user_channel_id = int(config['Channels']['user_channel_id'])
search_string = config['Settings']['search_string']
custom_message = config['Settings']['custom_message']

client = TelegramClient(session_name, api_id, api_hash)
client.start()


async def get_last_message_with_string():
    """
    Recupera a mensagem mais recente contendo a string de busca especificada
    do canal definido.

    Returns:
        Message: A mensagem mais recente que corresponde à string de busca.
    """
    async for message in client.iter_messages(channel_id, limit=100, search=search_string):
        return message


async def reply_other_chat(peer_user, reply_to_peer_id, topic_id=None):
    """
    Envia uma mensagem personalizada como resposta a uma mensagem em outro chat,
    referenciando uma mensagem do canal monitorado.

    Args:
        peer_user (InputPeer): A entidade do usuário para quem a resposta é enviada.
        reply_to_peer_id (InputPeer): O canal onde a mensagem original está localizada.
        topic_id (int, opcional): ID da mensagem principal no tópico se a resposta
        for em um tópico específico.
    """
    message = await get_last_message_with_string()
    reply_to = InputReplyToMessage(
        reply_to_msg_id=message.id,
        top_msg_id=topic_id,
        reply_to_peer_id=reply_to_peer_id
    )

    await client(SendMessageRequest(
        peer=peer_user,
        message=custom_message,
        reply_to=reply_to
    ))


@client.on(events.NewMessage(incoming=True, chats=[reply_channel_id]))
async def monitor_topics(event):
    """
    Monitora novas mensagens no canal de tópicos especificado, recupera
    o ID da mensagem respondida e aciona a função de resposta automática.

    Args:
        event (NewMessage.Event): O evento acionado por uma nova mensagem recebida.
    """
    topic_id = event.message.reply_to_msg_id
    original_message = await event.get_reply_message()
    if original_message:
        if isinstance(original_message, list):
            original_message = original_message[0]
        topic_id = original_message.id

    peer_user = await event.get_chat()
    reply_to_peer_id = await client.get_input_entity(channel_id)
    await reply_other_chat(peer_user, reply_to_peer_id, topic_id)


client.run_until_disconnected()
