
# 📢 PromoteBot
<img src="https://raw.githubusercontent.com/cleitonleonel/PromoteBot/master/promote_bot.png" alt="PromoteBot" width="250"/>

PromoteBot é um bot de usuário do Telegram projetado para engajamento e divulgação estratégica em fóruns do Telegram. Com monitoramento contínuo e respostas automáticas, este bot ajuda a amplificar mensagens, centralizar conteúdo e promover visibilidade em discussões.

## ✨ Descrição

Este bot de usuário do Telegram é uma ferramenta automatizada desenvolvida para engajamento e divulgação estratégica em fóruns do Telegram. Utilizando uma lógica de monitoramento contínuo, o bot detecta novas mensagens em tópicos específicos de um canal de discussão, onde o usuário é membro. Ao identificar uma nova publicação, o bot responde automaticamente com uma mensagem predefinida, citando uma mensagem de outro canal de referência. Isso permite que o bot replique e centralize conteúdos, estimulando interação e aumentando a visibilidade do material compartilhado.

---

## 📦 Instalação

Para instalar o PromoteBot, você pode clonar o repositório diretamente ou instalar via `pip`.

### Clonar o repositório
```bash
git clone https://github.com/cleitonleonel/PromoteBot.git
cd PromoteBot
pip install poetry
poetry install
```

### Usar `pip` diretamente com o repositório
```bash
pip install git+https://github.com/cleitonleonel/PromoteBot.git
```

---

## 🚀 Uso

1. **Configuração**: Defina as variáveis necessárias, como `api_id`, `api_hash`, `session_name`, IDs dos canais e a mensagem personalizada de divulgação.
2. **Rodando o Bot**: Após configurar o bot, execute o comando abaixo:
   ```bash
   poetry run python main.py
   ```
3. **Funcionalidade**:
   - O bot monitora o canal especificado em `reply_channel_id` e comenta automaticamente às mensagens detectadas com o conteúdo da `custom_message`.
   - O bot buscará a frase definida em `search_string` e, ao encontrá-la, enviará um comentário como resposta no canal de destino, reforçando a divulgação.

---

## ⚙️ Configuração

Antes de rodar o bot, configure as seguintes variáveis no código:

- `api_id`: O ID da API do Telegram.
- `api_hash`: O hash da API do Telegram.
- `session_name`: Nome da sessão para autenticação.
- `reply_channel_id`: ID do canal onde o bot deve monitorar mensagens.
- `channel_id`: ID do canal de onde as mensagens serão replicadas.
- `user_channel_id`: ID do canal do usuário.
- `search_string`: Texto ou frase para monitoramento.
- `custom_message`: Mensagem personalizada que o bot enviará junto à resposta.

Essas configurações podem ser feitas diretamente no código ou em um arquivo `.ini` para maior segurança.

---

## 💻 Desenvolvimento

Este projeto utiliza [Poetry](https://python-poetry.org/) para gerenciar as dependências e facilitar o ambiente de desenvolvimento.

### Rodando o projeto no modo desenvolvimento
1. Clone o repositório.
2. Instale as dependências com o Poetry:
   ```bash
   poetry install
   ```
3. Execute o bot:
   ```bash
   poetry run python app.py
   ```

### Testes
Para rodar os testes (se houver), utilize:
```bash
poetry run pytest
```

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar *issues* e *pull requests*.

---

**PromoteBot** – Automatize sua divulgação no Telegram com inteligência e eficácia!

# Desenvolvido por:

Cleiton Leonel Creton ==> cleiton.leonel@gmail.com
