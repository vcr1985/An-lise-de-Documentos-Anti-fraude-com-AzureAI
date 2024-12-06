import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from ultils.config import config

def upload_blob(file, file_name):
    try:
        # Validar configurações
        if not config.AZURE_CONNECTION_STRING or not config.CONTAINER_NAME:
            st.error("Configurações de conexão com o Azure Blob Storage estão ausentes.")
            return None

        # Inicializar o cliente do Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(config.AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=config.CONTAINER_NAME, blob=file_name)

        # Fazer o upload do blob
        file_content = file.read()  # Certificar que o conteúdo está em bytes
        blob_client.upload_blob(file_content, overwrite=True)

        # Retornar a URL do blob
        return blob_client.url
    except Exception as ex:
        st.error("Ocorreu um erro ao enviar o arquivo. Tente novamente mais tarde.")
        st.write(f"Detalhes do erro: {ex}")  # Apenas para desenvolvedores
        return None
