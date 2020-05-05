import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

import 'vuetify/dist/vuetify.min.css';
import colors from 'vuetify/lib/util/colors';
import Dialog from '@/components/dialog.js';

Vue.use(Dialog, vuetify)

import { TiptapVuetifyPlugin } from 'tiptap-vuetify'
import 'tiptap-vuetify/dist/main.css'


let vuetify = new Vuetify({
    theme: {
        base: colors.cyan.base
    }
});

Vue.use(TiptapVuetifyPlugin, {
    vuetify,
    iconsGroup: 'mdi'
  })

export default vuetify
