import json
import boto3
import uuid

# Inicializa os clientes AWS
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    model_id = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
    bucket_nome = "sentinel-deploy-codes" # COLOQUE O NOME DO SEU BUCKET AQUI
    
    try:
        print("Iniciando processo Sentinel...")
        
        # 1. Configuração do Prompt
        system_prompt = "Você é um Engenheiro DevOps Sênior. Responda apenas com o código solicitado e uma breve explicação técnica. Use blocos de código formatados."
        pergunta_usuario = event.get('pergunta', 'Gere um main.tf básico.')

        corpo_prompt = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1500,
            "system": system_prompt,
            "messages": [{"role": "user", "content": pergunta_usuario}]
        }

        # 2. Chamada ao Claude 4.5
        response = bedrock.invoke_model(
            modelId=model_id,
            body=json.dumps(corpo_prompt)
        )
        
        response_body = json.loads(response.get('body').read())
        resposta_texto = response_body['content'][0]['text']
        
        # 3. Salvando no S3
        nome_arquivo = f"projeto-devops-{uuid.uuid4().hex[:6]}.tf"
        
        s3.put_object(
            Bucket=bucket_nome,
            Key=nome_arquivo,
            Body=resposta_texto,
            ContentType='text/plain'
        )

        print(f"Sucesso! Arquivo {nome_arquivo} salvo no S3.")
        
        return {
            "status": "Sucesso",
            "arquivo_gerado": nome_arquivo,
            "localizacao": f"s3://{bucket_nome}/{nome_arquivo}",
            "previa": resposta_texto[:100] + "..."
        }

    except Exception as e:
        print(f"Erro: {str(e)}")
        return {"status": "Erro", "detalhes": str(e)}
