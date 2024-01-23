odoo.define('odoo_external_api_access.api_interactive', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');

    var QWeb = core.qweb;
    var _t = core._t;

    var ApiInteractiveWidget = Widget.extend({
        template: 'odoo_external_api_access.api_templates',
        events: {
            'click .api-endpoint': '_onEndpointClick',
            'click .execute-api-btn': '_onExecuteApi',
            'click .api-history-item': '_onHistoryItemClick',
            'click .api-favorite-toggle': '_onFavoriteToggle',
            'input .api-search-filter': '_onSearchFilter',
        },

        init: function (parent, options) {
            this._super(parent);
            this.options = options || {};
        },

        start: function () {
            this._renderEndpoints();
            this._renderHistory();
            this._renderFavorites();
            return this._super.apply(this, arguments);
        },

        _renderEndpoints: function () {
            var self = this;
            ajax.jsonRpc(API_DOCUMENTATION_URL, 'call', {}).then(function (endpoints) {
                self.$el.find('.api-endpoint-list').html(QWeb.render('ApiEndpoints', {
                    endpoints: endpoints
                }));
            });
        },

        _renderHistory: function () {
            var history = this._getApiHistory();
            this.$el.find('.api-history-list').html(QWeb.render('ApiHistory', {
                history: history
            }));
        },

        _renderFavorites: function () {
            var favorites = this._getApiFavorites();
            this.$el.find('.api-favorites-list').html(QWeb.render('ApiFavorites', {
                favorites: favorites
            }));
        },

        _onEndpointClick: function (event) {
            var endpointId = $(event.currentTarget).data('endpoint-id');
            this._showEndpointDetails(endpointId);
        },

        _onExecuteApi: function (event) {
            var endpointId = $(event.currentTarget).data('endpoint-id');
            this._executeApiOperation(endpointId);
        },

        _onHistoryItemClick: function (event) {
            var requestId = $(event.currentTarget).data('request-id');
            this._showRequestDetails(requestId);
        },

        _onFavoriteToggle: function (event) {
            var endpointId = $(event.currentTarget).data('endpoint-id');
            this._toggleFavorite(endpointId);
        },

        _onSearchFilter: function (event) {
            var searchTerm = $(event.currentTarget).val();
            this._filterEndpoints(searchTerm);
        },

        _getApiHistory: function () {
            // Fetch history from local storage or backend
            return JSON.parse(localStorage.getItem(API_HISTORY) || '[]');
        },

        _getApiFavorites: function () {
            // Fetch favorites from local storage or backend
            return JSON.parse(localStorage.getItem(API_FAVORITES) || '[]');
        },

        _showEndpointDetails: function (endpointId) {
            // Fetch and display endpoint details
        },

        _executeApiOperation: function (endpointId) {
            // Execute the API operation and handle the response
        },

        _showRequestDetails: function (requestId) {
            // Fetch and display request details from history
        },

        _toggleFavorite: function (endpointId) {
            // Toggle the favorite status of an endpoint
        },

        _filterEndpoints: function (searchTerm) {
            // Filter the displayed endpoints based on the search term
        },

        _handleError: function (message) {
            Dialog.alert(this, message, {
                title: _t('API Error'),
            });
        },
    });

    core.action_registry.add('api_interactive_widget', ApiInteractiveWidget);

    return {
        ApiInteractiveWidget: ApiInteractiveWidget,
    };
});