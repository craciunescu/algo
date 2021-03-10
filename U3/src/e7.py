"""
    @author: David E. Craciunescu
      @date: 2021/02/22 (yyyy/mm/dd)

    7. In Abeceland, a city famous for its beautiful N squares and that even you
    may know, they have a very curious system of roads.

    The way it works is the following:
    - Each square is directly connected to all other squares that begin with a 
      letter that is in their name. For example, Ace Square has streets that go
      to any square whose name starts with A, C, or E. This way they would be
      connected to Cut Square, Coast Square or East Square, but not with Doom,
      Fall or Tiara Square.
    
    - The streets are one way and they follow the rule of the letters.
      For example, from Ace Square you can go to Cut Square, but not the other
      way around, since it doesn't comply with the rule.
    
    - Places like Ace Square and Cat Square are connected in both directions,
      since they both comply with the rule of letters.

    All these connections between the N squares are stored in a street map,
    represented by an adjacency matrix of size NxN. In this map, the value of
    Streets[p, q] indicates whether one can go from p to q.

    April 26th, feast of San Isidoro of Seville, patron of letters and computer
    scientists, is coming up. The city of Abeceland has decided to celebrate it
    in a rather peculiar way. They play to reverse the direction of all streets
    that connect their city. What a wonderful idea, isn't it?

    On that day one can't move from Ace Square to Cut Square anymore, but they
    will be able to go the other way around, from Cut Square to Ace Square.
    Obviously, Ace Square and Cat Square will still remain connected to each
    other.

    Our objective is to design a standard divide-and-conquer algorithm that,
    receiving the street map adjacency matrix as a parameter, returns the
    street map valid for the day of San Isiodoro de Seville.

    Analyze the complexity of the provided solution and indicate the data
    structures you have used.
"""