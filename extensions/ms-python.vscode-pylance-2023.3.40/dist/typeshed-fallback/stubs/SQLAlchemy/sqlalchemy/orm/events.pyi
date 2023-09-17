from typing import Any

from .. import event

class InstrumentationEvents(event.Events):
    def class_instrument(self, cls) -> None: ...
    def class_uninstrument(self, cls) -> None: ...
    def attribute_instrument(self, cls, key, inst) -> None: ...

class _InstrumentationEventsHold:
    class_: Any
    def __init__(self, class_) -> None: ...
    dispatch: Any

class InstanceEvents(event.Events):
    def first_init(self, manager, cls) -> None: ...
    def init(self, target, args, kwargs) -> None: ...
    def init_failure(self, target, args, kwargs) -> None: ...
    def load(self, target, context) -> None: ...
    def refresh(self, target, context, attrs) -> None: ...
    def refresh_flush(self, target, flush_context, attrs) -> None: ...
    def expire(self, target, attrs) -> None: ...
    def pickle(self, target, state_dict) -> None: ...
    def unpickle(self, target, state_dict) -> None: ...

class _EventsHold(event.RefCollection):
    class_: Any
    def __init__(self, class_) -> None: ...

    class HoldEvents: ...

    def remove(self, event_key) -> None: ...
    @classmethod
    def populate(cls, class_, subject) -> None: ...

class _InstanceEventsHold(_EventsHold):
    all_holds: Any
    def resolve(self, class_): ...

    class HoldInstanceEvents(_EventsHold.HoldEvents, InstanceEvents): ...
    dispatch: Any

class MapperEvents(event.Events):
    def instrument_class(self, mapper, class_) -> None: ...
    def before_mapper_configured(self, mapper, class_) -> None: ...
    def mapper_configured(self, mapper, class_) -> None: ...
    def before_configured(self) -> None: ...
    def after_configured(self) -> None: ...
    def before_insert(self, mapper, connection, target) -> None: ...
    def after_insert(self, mapper, connection, target) -> None: ...
    def before_update(self, mapper, connection, target) -> None: ...
    def after_update(self, mapper, connection, target) -> None: ...
    def before_delete(self, mapper, connection, target) -> None: ...
    def after_delete(self, mapper, connection, target) -> None: ...

class _MapperEventsHold(_EventsHold):
    all_holds: Any
    def resolve(self, class_): ...

    class HoldMapperEvents(_EventsHold.HoldEvents, MapperEvents): ...
    dispatch: Any

class SessionEvents(event.Events):
    def do_orm_execute(self, orm_execute_state) -> None: ...
    def after_transaction_create(self, session, transaction) -> None: ...
    def after_transaction_end(self, session, transaction) -> None: ...
    def before_commit(self, session) -> None: ...
    def after_commit(self, session) -> None: ...
    def after_rollback(self, session) -> None: ...
    def after_soft_rollback(self, session, previous_transaction) -> None: ...
    def before_flush(self, session, flush_context, instances) -> None: ...
    def after_flush(self, session, flush_context) -> None: ...
    def after_flush_postexec(self, session, flush_context) -> None: ...
    def after_begin(self, session, transaction, connection) -> None: ...
    def before_attach(self, session, instance) -> None: ...
    def after_attach(self, session, instance) -> None: ...
    def after_bulk_update(self, update_context) -> None: ...
    def after_bulk_delete(self, delete_context) -> None: ...
    def transient_to_pending(self, session, instance) -> None: ...
    def pending_to_transient(self, session, instance) -> None: ...
    def persistent_to_transient(self, session, instance) -> None: ...
    def pending_to_persistent(self, session, instance) -> None: ...
    def detached_to_persistent(self, session, instance) -> None: ...
    def loaded_as_persistent(self, session, instance) -> None: ...
    def persistent_to_deleted(self, session, instance) -> None: ...
    def deleted_to_persistent(self, session, instance) -> None: ...
    def deleted_to_detached(self, session, instance) -> None: ...
    def persistent_to_detached(self, session, instance) -> None: ...

class AttributeEvents(event.Events):
    def append(self, target, value, initiator) -> None: ...
    def append_wo_mutation(self, target, value, initiator) -> None: ...
    def bulk_replace(self, target, values, initiator) -> None: ...
    def remove(self, target, value, initiator) -> None: ...
    def set(self, target, value, oldvalue, initiator) -> None: ...
    def init_scalar(self, target, value, dict_) -> None: ...
    def init_collection(self, target, collection, collection_adapter) -> None: ...
    def dispose_collection(self, target, collection, collection_adapter) -> None: ...
    def modified(self, target, initiator) -> None: ...

class QueryEvents(event.Events):
    def before_compile(self, query) -> None: ...
    def before_compile_update(self, query, update_context) -> None: ...
    def before_compile_delete(self, query, delete_context) -> None: ...
