<template>
    <v-item 
        class="choice"
        ref="item"
        v-slot:default="{ active }"
        :value="value"
    >
        <v-card
            ref="card"
            :color="active ? 'primary' : 'white lighten-3'"
            @click="click"
            @keypress="click"
        >
            <div class="d-flex flex-wrap align-center">
                <v-avatar class="ma-3" size="125" tile>
                    <v-icon size="80" v-if="imgSrc === undefined">
                        mdi-selection-ellipse
                    </v-icon>
                    <v-img v-else :src="display(imgSrc)" :alt="imgAlt"></v-img>
                </v-avatar>
                <div>
                    <v-card-title
                        class="headline"
                        v-text="label"
                    ></v-card-title>
                </div>
            </div>
        </v-card>
    </v-item>
</template>

<script>
import image from "@/js/image.js";
export default {
    name: "Choice",
    props: ["value", "label", "imgSrc", "imgAlt"],
    data() {
        return {
            endpoint: process.env.VUE_APP_API_ENDPOINT,
        };
    },
    methods: {
        display(filename) {
            return image(this.endpoint, filename);
        },
        click(evt) {
            if (
                evt.code == "Space" ||
                evt.code == "Enter" ||
                evt.type == "click"
            ) {
                this.value.selected = !this.active;
                this.$refs.item.toggle();
            }
        },
    },
};
</script>
