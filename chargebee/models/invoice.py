import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Invoice(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", "discount_amount", "item_level_discount_amount", "description", "entity_description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "entity_id"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "entity_id", "discount_amount"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LineItemTier(Model):
      fields = ["line_item_id", "starting_unit", "ending_unit", "quantity_used", "unit_amount", "starting_unit_in_decimal", "ending_unit_in_decimal", "quantity_used_in_decimal", "unit_amount_in_decimal"]
      pass
    class LinkedPayment(Model):
      fields = ["txn_id", "applied_amount", "applied_at", "txn_status", "txn_date", "txn_amount"]
      pass
    class DunningAttempt(Model):
      fields = ["attempt", "transaction_id", "dunning_type", "created_at", "txn_status", "txn_amount"]
      pass
    class AppliedCredit(Model):
      fields = ["cn_id", "applied_amount", "applied_at", "cn_reason_code", "cn_create_reason_code", "cn_date", "cn_status"]
      pass
    class AdjustmentCreditNote(Model):
      fields = ["cn_id", "cn_reason_code", "cn_create_reason_code", "cn_date", "cn_total", "cn_status"]
      pass
    class IssuedCreditNote(Model):
      fields = ["cn_id", "cn_reason_code", "cn_create_reason_code", "cn_date", "cn_total", "cn_status"]
      pass
    class LinkedOrder(Model):
      fields = ["id", "document_number", "status", "order_type", "reference_id", "fulfillment_status", "batch_id", "created_at"]
      pass
    class Note(Model):
      fields = ["entity_type", "note", "entity_id"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class Einvoice(Model):
      fields = ["id", "status", "message"]
      pass

    fields = ["id", "po_number", "customer_id", "subscription_id", "recurring", "status", "vat_number", \
    "price_type", "date", "due_date", "net_term_days", "exchange_rate", "currency_code", "total", \
    "amount_paid", "amount_adjusted", "write_off_amount", "credits_applied", "amount_due", "paid_at", \
    "dunning_status", "next_retry_at", "voided_at", "resource_version", "updated_at", "sub_total", \
    "sub_total_in_local_currency", "total_in_local_currency", "local_currency_code", "tax", "first_invoice", \
    "new_sales_amount", "has_advance_charges", "term_finalized", "is_gifted", "generated_at", "expected_payment_date", \
    "amount_to_collect", "round_off_amount", "line_items", "discounts", "line_item_discounts", "taxes", \
    "line_item_taxes", "line_item_tiers", "linked_payments", "dunning_attempts", "applied_credits", \
    "adjustment_credit_notes", "issued_credit_notes", "linked_orders", "notes", "shipping_address", \
    "billing_address", "einvoice", "payment_owner", "void_reason_code", "deleted", "vat_number_prefix", \
    "channel"]


    @staticmethod
    def create(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices"), params, env, headers)

    @staticmethod
    def create_for_charge_items_and_charges(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","create_for_charge_items_and_charges"), params, env, headers)

    @staticmethod
    def charge(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","charge"), params, env, headers)

    @staticmethod
    def charge_addon(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","charge_addon"), params, env, headers)

    @staticmethod
    def create_for_charge_item(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","create_for_charge_item"), params, env, headers)

    @staticmethod
    def stop_dunning(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"stop_dunning"), params, env, headers)

    @staticmethod
    def import_invoice(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","import_invoice"), params, env, headers)

    @staticmethod
    def apply_payments(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"apply_payments"), params, env, headers)

    @staticmethod
    def sync_usages(id, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"sync_usages"), None, env, headers)

    @staticmethod
    def apply_credits(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"apply_credits"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("invoices"), params, env, headers)

    @staticmethod
    def invoices_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"invoices"), params, env, headers)

    @staticmethod
    def invoices_for_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"invoices"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("invoices",id), None, env, headers)

    @staticmethod
    def pdf(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"pdf"), params, env, headers)

    @staticmethod
    def download_einvoice(id, env=None, headers=None):
        return request.send('get', request.uri_path("invoices",id,"download_einvoice"), None, env, headers)

    @staticmethod
    def add_charge(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"add_charge"), params, env, headers)

    @staticmethod
    def add_addon_charge(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"add_addon_charge"), params, env, headers)

    @staticmethod
    def add_charge_item(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"add_charge_item"), params, env, headers)

    @staticmethod
    def close(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"close"), params, env, headers)

    @staticmethod
    def collect_payment(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"collect_payment"), params, env, headers)

    @staticmethod
    def record_payment(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"record_payment"), params, env, headers)

    @staticmethod
    def refund(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"refund"), params, env, headers)

    @staticmethod
    def record_refund(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"record_refund"), params, env, headers)

    @staticmethod
    def remove_payment(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"remove_payment"), params, env, headers)

    @staticmethod
    def remove_credit_note(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"remove_credit_note"), params, env, headers)

    @staticmethod
    def void_invoice(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"void"), params, env, headers)

    @staticmethod
    def write_off(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"write_off"), params, env, headers)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"delete"), params, env, headers)

    @staticmethod
    def update_details(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"update_details"), params, env, headers)

    @staticmethod
    def resend_einvoice(id, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"resend_einvoice"), None, env, headers)
