
import json

class Parser:
    def __init__(self, file_name: str):
        '''Todas as funções 'objetivo' dessa classe concatenam os seus resultados à variável self.answer.'''

        with open(file_name) as fin:
            content = json.loads(fin.read())

        self.data = content['data']

        self.sep = '\n\n' + 70*'=' + '\n\n'
        self.answer = f'\nArquivo de respostas do primeiro Mini-Projeto: Parsing de json{self.sep}'

    def objetivo1(self):
        '''Cria um conjunto e para cada filme no json adiciona no conjunto todos os filmes
        mencionados em 'title', 'previousMovies' de cada ator, e 'nominees' de cada prêmio'''

        all_movies = set()

        for movie in self.data['movies']:

            all_movies.add(movie['title'])

            for actor in movie['cast']:
                for previous in actor['previousMovies']:        
                    all_movies.add(previous['title'])

            for award in movie['awards']:
                for nominee in award['nominees']:
                    all_movies.add(nominee)

        s = '\n\t'.join(all_movies)

        self.answer += f'Listar todos os títulos de filmes:\n\n\t{s}{self.sep}'

    def objetivo2(self):
        '''Cria um conjunto e para cada série no json adiciona no conjunto todas as séries
        mencionados em 'title', 'previousShows' de cada ator, e 'nominees' de cada prêmio.'''

        all_series = set()

        for show in self.data['series']:

            all_series.add(show['title'])

            for actor in show['cast']:
                for previous in actor['previousShows']:
                    all_series.add(previous['title'])

            for award in show['awards']:
                for nominee in award['nominees']:
                    all_series.add(nominee)

        s = '\n\t'.join(all_series)

        self.answer += f'Listar todas as séries:\n\n\t{s}{self.sep}'

    def objetivo3(self):
        '''Salva um valor pequeno como máximo e sempre que encontrar um valor maior que o máximo 
        sobreescreve o valor máximo e o nome da melhor obra encontrada.'''

        best_rating = -1
        best_cinema = 'Não há dados.'

        for value in self.data.values():
            for cinema in value:
                if cinema['rating'] > best_rating:
                    best_rating = cinema['rating']
                    best_cinema = cinema['title']

        self.answer += f'Recuperar filme/série com a melhor nota:\n\n\t{best_cinema}{self.sep}'

    def objetivo4(self):
        '''Para cada obra adiciona os gêneros dela em um conjunto.'''

        all_genres = set()

        for value in self.data.values():
            for cinema in value:
                all_genres.update(cinema['genres'])

        s = '\n\t'.join(all_genres)

        self.answer += f'Listar os gêneros de todos os filmes e séries:\n\n\t{s}{self.sep}'

    def objetivo5(self):
        '''Salva o tamanho da lista de filmes e da lista de séries somadosi.'''

        total_n = 0

        for value in self.data.values():
            total_n += len(value)

        self.answer += f'Obter o número total de filmes e séries:\n\n\t{total_n}{self.sep}'

    def objetivo6(self):
        '''Para cada obra adiciona todas as plataformas de streaming mencionadas em um conjunto.'''

        all_streamings = set()

        for value in self.data.values():
            for cinema in value:
                all_streamings.update(cinema['streaming'])

        s = '\n\t'.join(all_streamings)

        self.answer += f'Listar todas as plataformas de streaming disponíveis:\n\n\t{s}{self.sep}'

    def objetivo7(self):
        '''Adiciona em um conjunto todas as obras que mencionam Netflix e estão disponíveis
        e possuem a resolução 4K disponível.'''

        netflix_4k = []

        for value in self.data.values():
            for cinema in value:
                if 'Netflix' in cinema['streaming']:
                    if cinema['streaming']['Netflix']['available']:
                        if '4K' in cinema['streaming']['Netflix']['resolution']:
                            netflix_4k.append(cinema['title'])

        s = '\n\t'.join(netflix_4k)

        self.answer += f'Filtrar filmes/séries disponíveis em 4K no Netflix:\n\n\t{s}{self.sep}'

    def objetivo8(self):
        '''Cria um dicionário que para cada obra cria outro dicionário que relaciona uma plataforma de
        streaming disponível com o seu url.'''

        available_in = {}

        for value in self.data.values():
            for cinema in value:
                for platform_name in cinema['streaming']:
                    platform = cinema['streaming'][platform_name]
                    if platform['available']:
                        available_in.setdefault(cinema['title'], {}).setdefault(platform_name, platform['url'])

        s = '\n\t'.join([f'{j[0]}:\n\t\t'+'\n\t\t'.join([f'{i[0]}: {i[1]}' for i in j[1].items()]) for j in available_in.items()])

        self.answer += f'Identificar plataformas onde um filme específico está disponível:\n\n\t{s}{self.sep}'

    def objetivo9(self):
        '''Cria um dicionário que para cada ator mencionado cria outro dicionário que relaciona os
        filmes nos quais o ator participou com uma lista de personagens interpretados em cada filme
        (há casos raros em que um ator tem mais de um personagem em um filme).'''

        characters = {}

        for value in self.data.values():
            for cinema in value:
                for actor in cinema['cast']:
                    characters.setdefault(actor['actor'], {}).setdefault(cinema['title'], []).append(actor['character'])

        s = '\n\t'.join([f'{j[0]}:\n\t\t'+'\n\t\t'.join([f'{i[0]}:\n\t\t\t'+'\n\t\t\t'.join([k for k in i[1]]) for i in j[1].items()]) for j in characters.items()])

        self.answer += f'Listar todos os atores e os personagens que interpretam:\n\n\t{s}{self.sep}'

    def objetivo10(self):
        '''Salva um valor pequeno como máximo e sempre que encontrar um valor maior que o máximo 
        sobreescreve o valor máximo e o nome do ator com o maior salário.'''

        biggest_salary = -1
        richest_actor = 'Não há dados'

        for value in self.data.values():
            for cinema in value:
                for actor in cinema['cast']:
                    if actor['salary'] > biggest_salary:
                        biggest_salary = actor['salary']
                        richest_actor = actor['actor']

        self.answer += f'Obter o ator com o maior salário em um filme ou série:\n\n\t{richest_actor}{self.sep}'

    def objetivo11(self):
        '''Adiciona cada localização das listas de locais de filmagem em um conjunto.'''

        all_locations = set()

        for movie in self.data['movies']:
            for location in movie['production']['filmingLocations']:
                all_locations.add(location)

        s = '\n\t'.join(all_locations)

        self.answer += f'Listar todas as localizações de filmagens dos filmes:\n\n\t{s}{self.sep}'

    def objetivo12(self):
        '''Adiciona em um dicionário uma lista de diretores para cada filme'''

        movie_directors = {}

        for movie in self.data['movies']:
            movie_directors[movie['title']] = movie['directors']

        s = '\n\t'.join([f'{i[0]}:\n\t\t'+'\n\t\t'.join([f'{j}' for j in i[1]]) for i in movie_directors.items()])

        self.answer += f'Listar os diretores de cada filme:\n\n\t{s}{self.sep}'

    def objetivo13(self):
        '''Salva um valor pequeno como máximo e sempre que encontrar um valor maior que o máximo 
        sobreescreve o valor máximo e o nome do filme com maior receita.'''

        biggest_revenue = -1
        richest_movie = 'Não há dados'

        for movie in self.data['movies']:
            if movie['production']['boxOffice']['revenue'] > biggest_revenue:
                biggest_revenue = movie['production']['boxOffice']['revenue']
                richest_movie = movie['title']

        self.answer += f'Obter filme com maior receita na bilheteria:\n\n\t{richest_movie}{self.sep}'

    def objetivo14(self):
        '''Para cada filme soma o valor do lucro a um valor total e depois divide o total pelo número de filmes.'''

        n_profits = 0
        total_profit = 0

        for movie in self.data['movies']:
            n_profits += 1
            total_profit += movie['production']['boxOffice']['profit']

        mean_profit = total_profit / n_profits

        self.answer += f'Calcular lucro médio dos filmes:\n\n\t{mean_profit:.2f}{self.sep}'

    def objetivo15(self):
        '''Para cada filme salva o dicionário da distribuição de vendas.'''

        ticket_distribution = {}

        for movie in self.data['movies']: 
            ticket_distribution[movie['title']] = movie['production']['boxOffice']['ticketSales']

        s = '\n\t'.join([f'{i[0]}:\n\t\t'+'\n\t\t'.join([f'{j[0]}: {j[1]}' for j in i[1].items()]) for i in ticket_distribution.items()])

        self.answer += f'Obter a distribuição de venda de ingressos por região:\n\n\t{s}{self.sep}'

    def objetivo16(self):
        '''Para cada prêmio de cada obra salva uma lista das categorias em que a obra foi nomeada.'''

        cinema_awards = {}

        for value in self.data.values():
            for cinema in value:
                for award in cinema['awards']:
                    cinema_awards.setdefault(cinema['title'], {}).setdefault(award['award'], []).append(award['category'])

        s = '\n\t'.join([f'{j[0]}:\n\t\t'+'\n\t\t'.join([f'{i[0]}:\n\t\t\t'+'\n\t\t\t'.join([k for k in i[1]]) for i in j[1].items()]) for j in cinema_awards.items()])

        self.answer += f'Listar todos os prêmios e categorias de cada filme/série:\n\n\t{s}{self.sep}'

    def objetivo17(self):
        '''Se a obra tiver ganhado qualquer prêmio salva ela em uma lista.'''

        winning_cinema = []

        for value in self.data.values():
            for cinema in value:
                won = False
                for award in cinema['awards']:
                    if award['won']:
                        won = True
                if won:
                    winning_cinema.append(cinema['title'])

        s = '\n\t'.join(winning_cinema)

        self.answer += f'Identificar filmes/séries que ganharam prêmios:\n\n\t{s}{self.sep}'

    def objetivo18(self):
        '''Para cada ano salva um conjunto de todos os filmes nomeados à categoria
        de melhor filme em qualquer prêmio.'''

        best_nominees = {}

        for movie in self.data['movies']:
            for award in movie['awards']:
                if award['category'] == 'Best Picture':
                    best_nominees.setdefault(award['year'],set()).update(set(award['nominees']))

        s = '\n\t'.join([f'{i[0]}:\n\t\t'+'\n\t\t'.join([f'{j}' for j in i[1]]) for i in best_nominees.items()])

        self.answer += f'Listar os indicados ao prêmio de \'Melhor Filme\' de cada ano:\n\n\t{s}{self.sep}'

    def objetivo19(self):
        '''Salva um valor pequeno como máximo e sempre que encontrar um valor maior que o máximo 
        sobreescreve o valor máximo e o comentário mais votado.'''

        most_votes = -1
        helpful_comment = 'Não há dados'

        for value in self.data.values():
            for cinema in value:
                for review in cinema['reviews']:
                    if review['details']['helpfulVotes'] > most_votes:
                        most_votes = review['details']['helpfulVotes']
                        helpful_comment = review['comment']

        self.answer += f'Obter o comentário com o maior número de votos úteis:\n\n\t{helpful_comment}{self.sep}'

    def objetivo20(self):
        '''Para cada filme soma o valor da nota a um valor total e depois divide o total pelo número de filmes.'''

        n_ratings = 0
        total_ratings = 0

        for movie in self.data['movies']:
            n_ratings += 1
            total_ratings += movie['rating']

        mean_rating = total_ratings / n_ratings

        self.answer += f'Calcular a nota média dos filmes:\n\n\t{mean_rating}{self.sep}'

    def objetivo21(self):
        '''Analisa a data de publicação e salva as anteriores a 2022-01-01 em uma lista.'''

        comments = []

        for value in self.data.values():
            for cinema in value:
                for review in cinema['reviews']:
                    if review['details']['date'] < '2022-01-01':
                        comments.append(review['comment'])

        s = '\n\t'.join(comments)

        self.answer += f'Filtrar todas as avaliações feitas antes de 2022:\n\n\t{s}{self.sep}'

    def generate_file(self,output_name: str):
        '''Gera o arquivo com nome output_name e o conteúdo atual de self.answer e reseta o valor de self.answer.'''

        with open(output_name,'w') as file:
            file.write(self.answer)

        self.answer = f'\nArquivo de respostas do primeiro Mini-Projeto: Parsing de json{self.sep}'

    def clear_answer(self):
        '''Reseta o valor de answer para apenas no cabeçalho.'''

        self.answer = f'\nArquivo de respostas do primeiro Mini-Projeto: Parsing de json{self.sep}'

    def show_answer(self):
        '''Printa o estado atual da variável self.answer.'''

        print(answer)


if __name__ == '__main__':
    parser = Parser('movies_and_series.json')
    
    for i in range(1,22):
        exec(f'parser.objetivo{i}()')
    
    parser.generate_file('answer.txt')
