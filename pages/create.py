import streamlit as st
from datetime import datetime
from random import choice
from time import sleep
import json
import os
from config import pages
from config.configset import is_emoji


def success_messages():
    """
    Função responsável por exibir mensagens de sucesso caso a verificação
    funcione corretamente.
    """

    with st.spinner("Carregando..."):
        st.toast("Blog enviado com sucesso! 🎉", icon="✅")
        st.success("Recarregando a página para você continuar sua aventura bloguística... 🚀")
        sleep(2)
        st.rerun()


def blog_text():
    """
    Função responsável por exibir sobre a criação de blogs
    """

    st.title("📝 Criação de Blogs")
    st.write("Olá!!! Muito bom te ver aqui! Você se interessou pela criação de Blogs? Aqui é o lugar certo! No campo do formulário, você deve colocar o título do seu blog, uma descrição e até um ícone para dar um charme! Quero ver você criar blogs super legais! Ahhh, e quando acabar de criar seu blog, clique no botão de enviar dados e compartilhe o Blog com seus amigos!")
    st.badge("Certifique-se de preencher todos os campos!", color="red", icon="❗")

    st.divider()


def blog_creation():
    """
    Função responsável por criar os blogs e guardar arquivos
    no banco de dados local
    """

    with st.container(border=True):
        st.title("⭐ Formulário")
        col1, col2 = st.columns([1, 1])

        # Bloco de título
        with col1:
            st.subheader("Título")
            title = st.text_input("🌟 Dê sentido ao seu blog!")

        # Bloco de ícone
        with col2:
            st.subheader("Ícone")
            icon = st.text_input("🎨 Essencial para a estética!", max_chars=2)

        # Bloco de conteúdo
        st.subheader("Conteúdo")
        content = st.text_area("🤯 Sobre o que é seu blog?", height=215)

        # Bloco para enviar os dados para o banco de dados
        submit_button = st.button("Enviar dados 🚀")
        if submit_button:
            if title != "" and content != "" and is_emoji(icon):
                next_blog = pages.return_next_blog()
                os.mkdir(f"database/pages/{next_blog}")
                date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

                # Cria o arquivo de Blog python principal
                with open(f"pages/blogs/{next_blog}.py", "w", encoding="utf-8") as f:
                    f.write(f"""import streamlit as st

title = "{title}"
content = "{content}"
date = "{date}"

with st.container(border=True):

    st.title(f"{title} {icon}")
    st.caption(f"Data de criação: {date}")

    st.divider()

    st.caption(content)

data = f'''{title}\n\n{content}'''
st.download_button("Fazer download do Blog em um arquivo .txt", data, "blog.txt")

""")

                # Cria o arquivo de dados do Blog
                data = {"title": title}
                with open(f"database/pages/{next_blog}/data.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)

                # Cria o arquivo de ícone do Blog
                with open(f"database/pages/{next_blog}/icon.txt", "w", encoding="utf-8") as f:
                    f.write(icon)

                # Exibe a mensagem de sucesso
                success_messages()
            else:
                st.error("Por favor, preencha todos os campos corretamente para o seu blog brilhar! 🌟")


def instructions():
    with st.popover(":material/help: Instruções", use_container_width=True):
        st.caption("A seguir, confira as intruções de como fazer o seu blog.")

        # Instruções
        st.markdown("1. Preencha todos os campos do formulário corretamente. O título será exibido na barra literal, juntamente com o ícone. O conteúdo será o conteúdo principal do blog, que só será visível após entrar dentro daquele blog. O campo do ícone é muito importante, você deve pôr apenas UM ícone. Mas atenção: Alguns ícones não são compatíveis!")
        st.image("assets/create/create1.png", caption="Campos preenchidos corretamente")

        st.markdown("2. Após preencher todos os campos, clique no botão de Enviar dados 🚀.")
        st.image("assets/create/create2.png", caption="Botão de Enviar dados", use_container_width=True)

        st.markdown("3. Espere o programa verificar os dados e carregar.")
        st.image("assets/create/create3.png", caption="Análise dos campos do formulário", use_container_width=True)

        st.markdown("4. Após o programa verificar os dados e aceitar os campos do seu blog, o blog será exixido na barra lateral esquerda, e você pode clicar e ver seu blog!")
        st.image("assets/create/create4.png", caption="Blog disponível na barra lateral esquerda", use_container_width=True)



def main():
    blog_text()
    blog_creation()
    instructions()


main()
