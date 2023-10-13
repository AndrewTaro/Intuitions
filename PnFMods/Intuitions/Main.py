API_VERSION = 'API_v1.0'
MOD_NAME = 'Intuitions'

class Intuitions:
    def __init__(self, *args):
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)
        flash.setUbMarkup('IntuitionsUb.xml', 'IntuitionsUb.swf', 'Intuitions')

    def onBattleStart(self, *args):
        entity = dataHub.getSingleEntity('alertIndication')
        self.indicationComponent = [component for component in entity.components.values() if component.className == 'alertIndication'][0]
        self.indicationComponent.evIntuitionActiveChanged.add(self.onIntuitionActiveChanged)

    def onIntuitionActiveChanged(self, component):
        #print(component.intuitionActive)
        num = component.intuitionActive
        flash.setUbData({'Intuitions_intuitionsNum': num})
    
    def onBattleQuit(self, *args):
        flash.setUbData({'Intuitions_intuitionsNum': 0})
        self.indicationComponent = None

gIntuitions = Intuitions()