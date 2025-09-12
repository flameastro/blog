import json

def return_next_blog():
    """
    Função responsável por criar e salvar num arquivo a
    proxima página de blog para uso.

    Apenas é feita a chamada de função e é salvo no arquivo json.
    """

    try:
        with open("database/pages/next_blog.json", "r", encoding="utf-8") as f:
            number_next_blog = int(json.load(f)['next_blog'][4:]) + 1

        data = {
            'next_blog': f'blog{number_next_blog}'
        }

        with open("database/pages/next_blog.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return f'blog{number_next_blog}'
    except:
        data = {
            'next_blog': 'blog1'
        }

        with open("database/pages/next_blog.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return 'blog1'
