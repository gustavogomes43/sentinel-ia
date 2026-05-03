import boto3
import base64
import json

def lambda_handler(event, context):
    # 1. Conectar aos serviços
    s3 = boto3.client('s3')
    bedrock = boto3.client(service_name='bedrock-runtime')
    
    # 2. Pegar a imagem que acabou de cair no S3 (Vem do evento)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    image_bytes = response['Body'].read()
    
    # 3. Converter imagem para Base64
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')
    
    # 4. Configurar o corpo da requisição para o Claude 3 Haiku
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", # ou png
                            "data": encoded_image
                        }
                    },
                    {
                        "type": "text",
                        "text": "Você é um vigilante digital. Analise esta imagem de segurança. Se houver qualquer ameaça (armas, invasão, briga), responda apenas 'ALERTA'. Se estiver tudo calmo, responda 'NORMAL'."
                    }
                ]
            }
        ]
    })

    # 5. Chamar o Bedrock
    model_id = 'anthropic.claude-3-haiku-20240307-v1:0'
    
    response_bedrock = bedrock.invoke_model(body=body, modelId=model_id)
    response_body = json.loads(response_bedrock.get('body').read())
    
    resultado = response_body['content'][0]['text']
    
    print(f"Resultado da análise: {resultado}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'analise': resultado})
    }
