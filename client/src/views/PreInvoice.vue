<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        Pre Invoice
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search (Item number, Total Yard etc..)"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :loading="test"
        :headers="headers"
        :items="desserts"
        :search="search"
      >
        <template v-slot:item.action="{ item }">
          <v-btn
            dark
            x-small
            text
            color="black"
            @click="getPDF(item.Order_No)"
          >
            <v-icon>description</v-icon>
          </v-btn>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
export default {
  name: "received",
  data() {
    return {
      test: false,
      search: "",
      headers: [
        {
          text: "Order No",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Returned From", value: "Returned_From" },
        { text: "Return Date", value: "Return_Date" },
        { text: "Ref", value: "Ref" },
        { text: "Item Number", value: "Item_Number" },
        { text: "Equipment", value: "Equipment" },
        { text: "Weight", value: "Weight" },
        { text: "Grade", value: "Grade" },
        { text: "Connection", value: "Connection" },
        { text: "Inspection Specification", value: "Inspection_Specification" },
        { text: "PDF", value: "action", sortable: false }
      ],
      desserts: [
        {
          name: "OWS278TBG.01",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%"
        },
        {
          name: "OWS278TBG.02",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%"
        },
        {
          name: "OWS278TBG.03",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%"
        },
        {
          name: "OWS278TBG.04",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%"
        },
        {
          name: "OWS278TBG.05",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%"
        }
      ]
    };
  },
  computed: {
    ...mapGetters(["getUsername"])
  },
  mounted() {
    this.test = true;
    axios
      .get("/getPreinv", {
        params: { username: this.$store.getters.getUsername }
      })
      .then(response => {
        console.log(response);
        this.desserts = response.data;
        this.test = false;
      });
  },
  methods: {
    getPDF(orderno) {
      console.log(orderno);
      this.test = true;
      axios
        .get("/getPreinvPDF", {
          params: { orderno: orderno }
        })
        .then(response => {
          this.test = false;
          window.open(response.data.pdflink, "_blank");
        });
    }
  }
};
</script>

<style>
</style>