# -*- coding: utf-8 -*-

def file_to_list(file_dir):
    """
    Función que dado la dirección de un fichero de texto plano, devuelve un
     una lista en la que cada elemento de la lista es una linea del fichero
    :param file_dir: String
    :return: List
    """
    # TODO


def split_list_football_players_features(list_players, separator):
    """
    Función que dada una lista con las características de los futbolistas,
    devuelve la misma lista en la que cada elemento es una lista con las
    características de los futbolistas
    :param list_players: List
    :param separator: String
    :return: List
    """
    # TODO


def get_top_goals_players(list_players, top_n):
    """
    Función que devuelve el Top N de jugadores que más goles han metido.
    La feature goles se encuentra en la posición 20 y el apodo del jugador
    en la posición 2
    :param list_players: List
    :param top_n: Int
    :return: List
    """
    # TODO


def get_players_by_team(list_players, team):
    """
    Funcion que devuelve en una lista el apodo de los futbolistas que han
    jugado en el equipo que se les pasa como parámetro, ordenado por el
    número de minutos que han jugado
    :param list_players: List
    :param team: String
    :return: List
    """
    # TODO

def write_list_to_file(list_to_write, file_dir):
    """
    Función que dada una lista y un nombre de fichero, escriba en el fichero
    cada elemento de la lista en una linea
    :param list_to_write: List
    :param file_dir: String
    """
    # TODO
     

# Programa Principal
if __name__ == '__main__':
    
    # Fichero a leer
    file_name = '.futbolistas.txt'
    
    # Creamos la lista de futbolistas
    list_football_players = file_to_list(file_dir=file_name)
    
    # Transformamos la lista de futbolistas en una lista de listas
    list_football_players = split_list_football_players_features(
            list_players=list_football_players, separator='::')
    
    # Obtenemos una lista con los 10 maximos goleadores
    top_scorers = get_top_goals_players(list_players=list_football_players, 
                                        top_n=10)
    
    # Obtenemos una lista con los jugadores de mi equipo de fútbol ordenado por lo minutos jugados
    players_team = get_players_by_team(list_players=list_football_players, 
                                       team='Rayo Vallecano')
    
    # Escribo en un fichero llamado "goleadores.txt" los 10 maximos goleadores
    write_list_to_file(top_scorers, 'goleadores.txt')
    
    
    # Escribo en un fichero llamado "jugadores_de_mi_equipo.txt" todos los jugadores de mi equipo de futbol ordenado
    # por el número de minutos que han jugado
    write_list_to_file(players_team, 'jugadores_de_mi_equipo.txt')
