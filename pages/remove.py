import streamlit as st
from time import sleep
import os


def content():
    """
    Função responsável por exibir o conteúdo da página.
    Isso é, aprpesentar em que local está e o que se pode fazer.
    """

    st.title("❌ Remoção de Blogs")
    st.caption("Olá! Você fez seu blog mas por algum motivo deseja deletar? Fique tranquilo, nesta página você consegue fazer isso facilmente! Abaixo há a página principal e existe também as instruções de como fazer cada etapa, fique a vontade para explorar!")

    st.divider()


def delete_blog():
    """
    Função responsável por verificar se o número do blog inserido
    existe. Caso exista, então o programa automaticamente deletará o blog.
    Caso não exista, ou por algum motivo der erro, então o usuário será
    informado com uma mensagem de erro.
    """

    # Adiciona o campo de pesquisa
    search_input = st.text_input(":material/search: Pesquisar")

    # Adiciona um efeito de vermelho para verde no badge (red -> green)
    with st.empty():
        st.badge(":material/checklist: Coloque um número válido de 0 a 9.", color="red")
        if search_input and search_input.isnumeric():
            st.badge(":material/checklist: Coloque um número válido de 0 a 9.", color="green")

    # Adiciona o botão de deletar o blog
    delete_button = st.button(":material/delete: Deletar", type="primary")
    if delete_button:
        if search_input.isnumeric():  # Verifica se o campo de pesquisa está correto
            try:
                with st.spinner("Analisando..."):
                    sleep(2)

                    os.remove(f"pages/blogs/blog{search_input}.py")
                    os.remove(f"database/pages/blog{search_input}/data.json")
                    os.remove(f"database/pages/blog{search_input}/icon.txt")
                    os.rmdir(f"database/pages/blog{search_input}")

                    st.success("Blog removido com sucesso...")
                    st.toast("Página prestes a recarregar.", icon="✅")
                    sleep(2)

                    st.rerun()

            except Exception as e:
                st.warning(f"Algo de errado aconteceu. Por favor, verifique novamente as informações. Erro: {e}")

        if not search_input.isnumeric():
            st.warning("Por favor, insira um número válido.")


    st.divider()


def instructions():
    """
    Função responsável por exibir as instruções ao usuário.
    Útil para pessoas com dificuldade em entendimento.
    Serve como auxiliar na tarefa de remoção de blogs.
    """

    with st.popover(":material/help: Instruções", use_container_width=True):
        st.markdown("1. Na barra lateral esquerda, verifique o número dentro dos parênteses logo após o título do blog. Coloque este número dentro do campo de pesquisa.")
        st.image("assets/remove/remove1.png", caption="Verifique o número na barra lateral esquerda e coloque no campo de pesquisa.", use_container_width=True)

        st.markdown("2. Em seguida, clique no botão de Deletar, e espere o programa analisar se este blog existe.")
        st.image("assets/remove/remove2.png", caption="Clique no botão de deletar.", use_container_width=True)

        st.markdown("3. Após o programa analisar se este blog realmente existe, ele te dará uma resposta. Se você fizer tudo certo, deverá ver que o blog sumiu da barra lateral esquerda.")
        st.image("assets/remove/remove3.png", caption="Aguarde o programa processar e retornar uma resposta.", use_container_width=True)





def main():
    content()
    delete_blog()
    instructions()


main()
