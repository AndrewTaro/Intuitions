API_VERSION = 'API_v1.0'
MOD_NAME = 'Intuitions'

try:
    import events, dataHub, ui, constants
except:
    pass

COMPONENT_KEY = 'modIntuitions'

class Intuitions:
    def __init__(self, *args):
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)

    def onBattleStart(self, *args):
        entity = dataHub.getSingleEntity('alertIndication')
        if entity is None:
            return
        self.indicationComponent = entity[constants.UiComponents.alertIndication]
        self.indicationComponent.evIntuitionActiveChanged.add(self.onIntuitionActiveChanged)

        self.entityId = ui.createUiElement()
        ui.addDataComponentWithId(self.entityId, COMPONENT_KEY, {'intuitionsCount': -1})

    def onIntuitionActiveChanged(self, component):
        num = component.intuitionActive
        ui.updateUiElementData(self.entityId, {'intuitionsCount': num})
    
    def onBattleQuit(self, *args):
        # Can be called when the client is shutting down, even without a battle!
        try:
            self.indicationComponent.evIntuitionActiveChanged.remove(self.onIntuitionActiveChanged)
            ui.deleteUiElement(self.entityId)
            self.indicationComponent = None
        except:
            pass


gIntuitions = Intuitions()