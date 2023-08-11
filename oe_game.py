import game_stats
import utils
still_running = 'y'

def main():

    while still_running == 'y':
        print(utils.title("NBA Offensive Efficiency (OE) Calculator - Game"))
        print("")
        name = input("What player do you want to review: ")
        fgm = utils.get_int(f"Enter total Field Goals made (including 3's): ")
        if fgm == 0:
            pass
        ass = utils.get_int(f"Enter total Assists: ")
        if ass == 0:
            pass
        fga = utils.get_int(f"Enter total Field Goals attempted (including 3's): ")
        if fga == 0:
            pass
        orb = utils.get_int(f"Enter total Offensive Rebounds: ")
        if orb == 0:
            pass
        to = utils.get_int(f"Enter total Turnovers: ")
        if to == 0:
            pass

        analysis = game_stats.OE(name)

        analysis.get_oe_stats(fgm, ass, fga, orb, to)
        analysis.calculate_oe(fgm, ass, fga, orb, to)
        
        print("")
        analysis.display_oe(fgm, ass, fga, orb, to)
        print("")
        again = input("Do you want to check another player (y for yes)?: ")
        print("")
        if again != 'y':
            print("See you next time!")
            break

main()
        
        
    
