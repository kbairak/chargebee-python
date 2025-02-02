import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class EntitlementOverride(Model):
    class EmbeddedResource(Model):
      fields = [""]
      pass

    fields = ["id", "entity_id", "entity_type", "feature_id", "feature_name", "value", "name", \
    "expires_at", "embedded"]


    @staticmethod
    def add_entitlement_override_for_subscription(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"entitlement_overrides"), params, env, headers)

    @staticmethod
    def list_entitlement_override_for_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"entitlement_overrides"), params, env, headers)
