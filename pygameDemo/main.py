from pygameDemo.game.war import PlaneWar

def main():
    war = PlaneWar()
    war.add_small_enemies(6)
    war.run_game()

if __name__ == '__main__':
    main()