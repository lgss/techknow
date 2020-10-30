<template>
    <v-item 
        class="choice"
        ref="item"
        v-slot:default="{ active }"
        :value="value"
    >
        <v-card ref="card" :color="active ? 'primary' : 'white'" @click="click"
            class="d-flex flex-wrap align-content-start justify-start" @keypress="click" height="100%">
            <div>
                <div class="ma-3" style="width:150px;height:150px">
                    <v-img v-if="imgSrc" :src="display(imgSrc)" :alt="imgAlt" :title="imgAlt" 
                        style="max-height:150px" ></v-img>
                    <v-icon size="80" v-else style="left:35px;top:35px">
                        mdi-arrow-right-bold-circle-outline
                    </v-icon>
                </div>
                <v-card-title
                    class="headline"
                    v-text="label"
                ></v-card-title>
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
                this.value.selected = !this.value.selected;
                this.$refs.item.toggle();
            }
        },
    },
};
</script>

<style scoped>
    .choice:focus {
        outline: -webkit-focus-ring-color auto 1px;
    }
</style>
