import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import light from './theme';

Vue.use(Vuetify);

import Dialog from '@/components/dialog.js';

Vue.use(Dialog, vuetify)

let vuetify = new Vuetify({
    theme: {
        themes: { light }
    },
});

export default vuetify
