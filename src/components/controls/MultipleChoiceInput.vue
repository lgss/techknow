<template>
    <v-input :rules="rules" :value="sel">
        <v-container max-width="1200" class="mx-auto">
            <div class="d-flex flex-wrap align-center">
                <div class="text-left">
                    <h2>{{ label }}</h2>
                    <h3>Please select one or more</h3>
                </div>
                <v-spacer></v-spacer>
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
            </div>
            <v-item-group v-model="sel" :class="name" multiple>
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
    name: "MultipleChoiceInput",
    props: ["label", "name", "img", "choices", "isMandatory"],
    components: {
        Choice,
    },
    data() {
        return {
            sel: [],
            rules: this.isMandatory
                ? [
                      (value) =>
                          !!value.length ||
                          "Please select at least one response",
                  ]
                : [],
            endpoint: process.env.VUE_APP_API_ENDPOINT,
        };
    },
    watch: {
        sel: function() {
            this.$emit("responded", this.sel);
        },
    },
    methods: {
        imgFromChoice(c) {
            return c.img === undefined ? undefined : c.img.src;
        },
        display(filename) {
            return image(this.endpoint, filename);
        },
    },
};
</script>
