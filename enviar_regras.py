import requests
import os

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

dados = {
    "username": "Regras PF",
    "embeds": [{
        "title": "📋・Regras Polícia Federal",
        "description": (
            "# Regras da Polícia Federal\n\n"
            "Para manter a organização, o respeito e o bom ambiente "
            "para todos, siga todas as regras abaixo.\n\n"
            "Ao permanecer na corporação, você concorda em cumprir "
            "as regras estabelecidas."
        ),
        "color": 3447003,
        "fields": [
            {
                "name": "👥・1. RESPEITO",
                "value": "Respeite todos os membros, jogadores e integrantes da equipe."
            },
            {
                "name": "🛡️・2. ROLEPLAY",
                "value": "Mantenha o RP de forma coerente e evite atitudes que prejudiquem a experiência dos demais."
            },
            {
                "name": "🚫・3. PROIBIÇÕES",
                "value": "É proibido utilizar cheats, exploits, bugs ou qualquer recurso que ofereça vantagem indevida."
            },
            {
                "name": "👮・4. HIERARQUIA",
                "value": "Respeite a hierarquia e siga as orientações dos superiores."
            },
            {
                "name": "📢・5. COMUNICAÇÃO",
                "value": "Utilize os canais corretos e evite spam, flood ou mensagens desnecessárias."
            }
        ],
        "footer": {
            "text": "Polícia Federal • Regras Oficiais"
        }
    }]
}

dados["embeds"][0]["description"] += (
    "\n\n🌐 **Leia todas as regras completas no site abaixo:**\n"
    "https://regras-pf-policiafederalmta.netlify.app"
)

resposta = requests.post(WEBHOOK_URL, json=dados)

if resposta.status_code == 204:
    print("✅ Regras enviadas com sucesso!")
else:
    print("❌ Erro:", resposta.status_code)
    print(resposta.text)
