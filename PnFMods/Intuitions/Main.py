API_VERSION = 'API_v1.0'
MOD_NAME = 'Intuitions'

try:
    import events, dataHub, ui
except:
    pass

PARAMETER_ID = 'modIntuitions'

class Intuitions:
    def __init__(self, *args):
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)

    def onBattleStart(self, *args):
        entity = dataHub.getSingleEntity('alertIndication')
        if entity is None:
            return
        self.indicationComponent = [component for component in entity.components.values() if component.className == 'alertIndication'][0]
        self.indicationComponent.evIntuitionActiveChanged.add(self.onIntuitionActiveChanged)

        self.entityId = ui.createUiElement()
        ui.addDataComponent(self.entityId, {'data': {'intuitionsCount': -1}})
        ui.addParameterComponent(self.entityId, PARAMETER_ID)

    def onIntuitionActiveChanged(self, component):
        num = component.intuitionActive
        ui.updateUiElementData(self.entityId, {'data': {'intuitionsCount': num}})
    
    def onBattleQuit(self, *args):
        try:
            self.indicationComponent.evIntuitionActiveChanged.remove(self.onIntuitionActiveChanged)
        except:
            pass
        ui.deleteUiElement(self.entityId)
        self.indicationComponent = None

gIntuitions = Intuitions()