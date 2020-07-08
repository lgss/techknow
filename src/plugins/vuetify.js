import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

import 'vuetify/dist/vuetify.min.css';
import Dialog from '@/components/dialog.js';

Vue.use(Dialog, vuetify)

let vuetify = new Vuetify({
    theme: {
        themes: { 
            light: {
                primary: "#1d5f7a",
                secondary: "#f7f7f7",
            }
        }
    },
});

export default vuetify
