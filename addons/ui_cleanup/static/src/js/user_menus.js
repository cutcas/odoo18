/** @odoo-module **/

import { UserMenu } from '@web/webclient/user_menu/user_menu';
import { patch } from '@web/core/utils/patch';
import { registry } from '@web/core/registry';

const userMenuRegistry = registry.category('user_menuitems');

/**
 * Remove unnecessary items from user menu (top right corner)
 * to provide a cleaner, more focused interface
 */
patch(UserMenu.prototype, {
  setup() {
    super.setup();
    // Remove documentation and support links
    userMenuRegistry.remove('documentation');
    userMenuRegistry.remove('support');

    // Remove shortcuts menu
    userMenuRegistry.remove('shortcuts');

    // Remove tour/onboarding
    userMenuRegistry.remove('web_tour.tour_enabled');

    // Remove separator
    userMenuRegistry.remove('separator');

    // Remove Odoo.com account link
    userMenuRegistry.remove('odoo_account');

    // Remove PWA installation option
    userMenuRegistry.remove('install_pwa');
  },
});
