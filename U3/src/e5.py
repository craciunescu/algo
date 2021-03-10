"""
    @author: David E. Craciunescu
      @date: 2021/02/22 (yyyy/mm/dd)

    5. In Aceland, the very celebrated national sport is tennis. The country
    keeps a ranking in which each player is assigned a number of points
    according to their quality as a player. In other words, the best player
    in the country is the one with the highest number of points.

    Every year a couple from Aceland competes in an international doubles
    tennis tournament, but the way the Acelandics select their best couple is
    a little peculiar, though.

    Each player's name is placed on a list in a random position, and each player
    can only compete with the players that are adjacent to them in the list. In
    other words, the ones in front of them and behind them on the list.

    Obviously, the first player on the list can only pair up with the second, 
    and the last player can only pair up with the one before them. The rest do 
    have two possible options to form a pair of doubles, the one before or the 
    one after them.
    
    With this seemingly nonsensical restriction and methodology, the Aceland 
    team chooses its best pair of players. What they do is count the sum of
    the points of each pair and select the pair with the greatest amount.

    Design a divide-and-conquer algorithm that shall help the Acelandics find
    their next pair of tennis champions, and analyze the complexity of the 
    provided solution.

"""