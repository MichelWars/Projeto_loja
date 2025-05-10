import google.generativeai as genai
import os

# Essa configuração é para utilizar o Gemini da Google para gerar a bio dos veículos automaticamente.
# link: https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br&amp%3Bauthuser=3&amp%3Blang=python&lang=python

def get_descricao_produto(produto, console, ano_lancamento):
    genai.configure(api_key="AIzaSyCpsGKqjQ_daC0G4yCGgzGST5galVhFTxk")
    # obs: Use uma variável de ambiente para a chave da API
    model = genai.GenerativeModel('gemini-1.5-flash') 
    
    prompt = (
        f"Crie uma descrição ou sobre o jogo {produto}, quando necessario use {console} e {ano_lancamento} para identificar a versão do jogo, caso aja varias versões com o mesmo titulo."
        f"Limite a descrição a 300 caracteres."
    )
    
    response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        max_output_tokens=300
        )
    )
    
    return response.text