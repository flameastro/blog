import streamlit as st
import json
from config import configset


configset.main()


def set_pages():
    """
    Função responsável por configurar as páginas do Blog.
    Organiza as páginas em seções diferentes, com listas dentro
    de dicionários.
    """

    # Cria o dicionário de páginas
    pages = {
        "🏠 Início": [
            st.Page("pages/welcome.py", title="Bem-vindo", icon="☃️")
        ],

        "🪄 Criação e Remoção": [
            st.Page("pages/create.py", title="Criar Blog", icon="✨"),
            st.Page("pages/remove.py", title="Remover Blog", icon="🗑️")
        ],

        "📱 Sistema": [
            st.Page("pages/about.py", title="Sobre", icon="🗨️")
        ],

        "🗒️ Blogs": []
    }

    # Bloco de código que adiciona as páginas de Blogs automaticamente
    limit = 15
    for i in range(1, limit+2):
        try:
            with open(f"database/pages/blog{i}/data.json", "r", encoding="utf-8") as f:
                title = json.load(f)["title"]

            with open(f"database/pages/blog{i}/icon.txt", "r", encoding="utf-8") as f:
                f.seek(0)
                icon = f.read()

            pages["🗒️ Blogs"].append(st.Page(f"pages/blogs/blog{i}.py", title=f"{title} ({i})", icon=icon))
        except:
            limit += 1

    # Adiciona navegação
    navigation = st.navigation(pages=pages)
    navigation.run()


def main():
    set_pages()


main()
