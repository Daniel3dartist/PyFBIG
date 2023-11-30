from ac import AC
from al import AL
from am import AM
from ap import AP
from ba import BA
from ce import CE
from df import DF
from es import ES
from go import GO
from ma import MA
from mg import MG
from ms import MS
from mt import MT
from pa import PA
from pb import PB
from pe import PE
from pi import PI
from pr import PR
from rj import RJ
from rn import RN
from ro import RO
from rr import RR
from rs import RS
from sc import SC
from se import SE
from sp import SP
from to import TO

"""
states_name = {
    'AC': {
        'name': "Acre",
        'acronym': 'AC',
        'state_class': AC()
    },
      'AL':{
          'name': "Alagoas",
          'acronym': 'AL',
          'state_class': AL(),
      },
      "Amapá",
      "Amazonas",
      "Bahia",
      "Ceará",
      "Distrito Federal",
      "Espírito Santo",
      "Goiás",
      "Maranhão",
      "Mato Grosso",
      "Mato Grosso do Sul",
      "Minas Gerais",
      "Pará",
      "Paraíba",
      "Paraná",
      "Pernambuco",
      "Piauí",
      "Rio de Janeiro",
      "Rio Grande do Norte",
      "Rio Grande do Sul",
      "Rondônia",
      "Roraima",
      "Santa Catarina",
      "São Paulo",
      "Sergipe",
      "Tocantins"
}
"""

class BRStates:
    def __init__(self):
#        self.states_name = states_name
        self.states = [AC, AM, AP, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE]


if __name__ == '__main__':
    br = BRStates()
#    print(br.states_name)
    for i in BRStates().states:
        if i().cities:
            print(i, i().cities)