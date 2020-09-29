<template>
    <v-input :rules="rules" :value="sel">
        <v-container max-width="1200" class="mx-auto">
            <div class="d-flex flex-wrap">
                <v-col cols=auto class="align-self-center">
                    <v-avatar class="ma-3" size="125" tile>
                        <v-icon size="80" v-if="img === undefined"
                            >mdi-comment-question-outline</v-icon
                        >
                        <v-img
                            v-else
                            :src="display(img.src)"
                            :alt="img.alt"
                        ></v-img>
                    </v-avatar>
                </v-col>
                <v-col sm=9 md=9 lg=9>
                    <div class="text-left">
                        <label ref="label" role="heading" aria-level="3" class="text-h4" v-text="label" tabindex="0"></label>
                        <div class="text-h6 mt-3" tabindex="0" v-if="example"><v-icon>mdi-information-outline</v-icon>{{example}}</div>
                        <div class="text-h5 font-weight-bold mt-3" tabindex="0">Please select one choice</div>
                    </div>
                </v-col>
            </div>
            <v-item-group v-model="sel" :class="name">
                <v-row dense>
                    <v-col
                        v-for="choice in choices"
                        :key="choice.value"
                        cols="12"
                    >
                        <choice
                            :value="choice"
                            :index="choice"
                            :label="choice.value"
                            :imgSrc="imgFromChoice(choice)"
                        />
                    </v-col>
                </v-row>
            </v-item-group>
        </v-container>
    </v-input>
</template>
<script>
import Choice from "@/components/controls/Choice.vue";
import image from "@/js/image.js";
export default {
    name: "SingleChoiceInput",
    props: ["label", "name", "example", "img", "choices", "isMandatory"],
    components: {
        Choice,
    },
    data() {
        return {
            sel: {},
            rules: this.isMandatory
                ? [
                      (choice) =>
                          (choice && choice.value !== undefined) ||
                          "Please select a response",
                  ]
                : [],
            endpoint: process.env.VUE_APP_API_ENDPOINT,
        };
    },
    watch: {
        sel: function() {
            this.$emit("responded", [this.sel]);
        },
    },
    methods: {
        imgFromChoice(c) {
            return c.img === undefined ? undefined : c.img.src;
        },
        display(filename) {
            return image(this.endpoint, filename);
        },
        focus() {
            this.$refs.label.focus()
        },
    },
};
</script>
