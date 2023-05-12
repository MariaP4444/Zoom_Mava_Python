
import view.zooView as zooView
import model.Zoo as zooModel

if __name__ == '__main__':
    zoo = zooModel.Zoo()
    view = zooView.zooView()
    view.menu_principalV(zoo)