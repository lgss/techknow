<template>
    <v-input :rules="rules" :value="sel">
        <v-container fluid>
            <div class="text-left">
                <h2>{{ label }}</h2>
                <h3>Please select one or more</h3>
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
                        />
                    </v-col>
                </v-row>
            </v-item-group>
        </v-container>
    </v-input>
</template>

<script>
import Choice from "@/components/controls/Choice.vue";

export default {
    name: "MultipleChoiceInput",
    props: ["label", "name", "choices", "isMandatory"],
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
        };
    },
    watch: {
        sel: function() {
            this.$emit("responded", this.sel);
        },
    },
};
</script>
