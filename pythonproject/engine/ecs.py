
class System:
    def __init__(self):
        """System()"""
        self.ecs = None
        self.game = None

    def update(self, *args):
        raise NotImplementedError

class Ecs:
    def __init__(self, game):
        """Ecs(game)"""
        self._game = game
        self._systems = []
        self._entities = {}
        self._dead_entities = set()
        self._components = {}
        self._next_entity_id = 0

    def delete_all(self):
        """delete_all()"""
        self._next_entity_id = 0
        self._components.clear()
        self._entities.clear()

    def add_system(self, system_instance, priority = 0):
        """add_system(system_instance, priority = 0)"""
        assert issubclass(system_instance.__class__, System)
        system_instance.priority = priority
        system_instance.ecs = self
        system_instance.game = self._game
        self._systems.append(system_instance)
        self._systems.sort( key = lambda sys: sys.priority, reverse = True )

    def delete_system(self, system_type):
        """delete_system(system_type)"""
        for system in self._systems:
            if type(system) == system_type:
                system.ecs = None
                system.game = None
                self._systems.remove(system)

    def get_system(self, system_type):
        """get_system(system_type)"""
        for system in self._systems:
            if type(system) == system_type:
                return system

    def create_entity(self, *components):
        """create_entity(*components)"""
        self._next_entity_id += 1
        for component in components:
            self.add_component(self._next_entity_id, component)
        return self._next_entity_id

    def delete_entity(self, entity, immediate = False):
        """delete_entity(entity, immediate = False)"""
        if immediate:
            for component_type in self._entities[entity]:
                self._components[component_type].discard(entity)
                if not self._components[component_type]:
                    del self._components[component_type]
            del self._entities[entity]
        else:
            self._dead_entities.add(entity)

    def add_component(self, entity, component):
        """add_component(entity, component)"""
        component_type = type(component)
        if component_type not in self._components:
            self._components[component_type] = set()
        self._components[component_type].add(entity)
        if entity not in self._entities:
            self._entities[entity] = {}
        self._entities[entity][component_type] = component

    def delete_component(self, entity, component_type):
        """delete_component(entity, component_type)"""
        self._components[component_type].discard(entity)
        if not self._components[component_type]:
            del self._components[component_type]
        del self._entities[entity][component_type]
        if not self._entities[entity]:
            del  self._entities[entity]
        return entity

    def component_for_entity(self, entity, component_type):
        """component_for_entity(entity, component_type)"""
        return self._entities[entity][component_type]

    def components_for_entity(self, entity):
        """components_for_entity(entity)"""
        return tuple(self._entities[entity].values())

    def has_component(self, entity, component_type):
        """has_component(entity, component_type)"""
        return component_type in self._entities[entity]

    def get_component(self, component_type):
        """get_component(component_type)"""
        for entity in self._components.get(component_type, []):
            yield entity, self._entities[entity][component_type]

    def get_components(self, *component_types):
        """get_components(*component_types)"""
        try:
            for entity in set.intersection(*[self._components[ct] for ct in component_types]):
                yield entity, [self._entities[entity][ct] for ct in component_types]
        except KeyError:
            pass

    def _update(self, *args):
        """_update(*args)"""
        if self._dead_entities:
            for entity in self._dead_entities:
                self.delete_entity(entity, immediate = True)
            self._dead_entities.clear()
        for system in self._systems:
            system.update(*args)
