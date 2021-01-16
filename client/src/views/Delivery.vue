<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <b>Delivery Ticket</b>
        <v-spacer></v-spacer>
        <v-card class="text-center">
        <v-dialog v-model="dialogg" width="300">
          <v-card>
            <v-list-item two-line class="light-blue lighten-4">
              <v-list-item-content>
                <v-list-item-title class="headline"></v-list-item-title>
                <v-list-item-subtitle>Order Number</v-list-item-subtitle>
                <v-list-item-title class="headline">{{
                  DTNO
                }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-divider></v-divider>
            <v-row align="center" justify="space-around">
              <v-btn
                :loading="dtpdfload"
                depressed
                color="white"
                block
                @click="getDTPDF"
              >
                DT summary/Tally report(.PDF)
              </v-btn>
              <v-btn
                :loading="dtpdfload"
                depressed
                color="white"
                block
                @click="getDTEXCEL"
              >
                Tally report(.XLSX)
              </v-btn>
              <v-btn
                :loading="dtpdfload"
                depressed
                color="white"
                block
                @click="getWire"
              >
                Wire Sling(.PDF)
              </v-btn>
            </v-row>
          </v-card>
        </v-dialog>
      </v-card>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search (DT number, Quantity etc..)"
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
          <v-btn dark x-small text color="black" @click="getDOC(item)">
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
  name: "delivery",
  data() {
    return {
      wiresling: '',
      dtpdfload: false,
      DTNO: '',
      test: false,
      search: "",
      dialogg: false,
      headers: [
        {
          text: "DT No",
          align: "start",
          sortable: true,
          value: "DT_No"
        },
        { text: "Sent To", value: "Sent_To" },
        { text: "Item No", value: "Item_No" },
        { text: "Quantity", value: "Quantity" },
        { text: "Rig", value: "Rig" },
        { text: "Equipment", value: "Equipment" },
        { text: "Weight", value: "Weight" },
        { text: "Grade", value: "Grade" },
        { text: "Connection", value: "DT_Connection" },
        { text: "Ref", value: "Ref" },
        { text: "PDF", value: "action", sortable: false },
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
      .get("/getDelivery", {
        params: { username: this.$store.getters.getUsername }
      })
      .then(response => {
        console.log(response);
        this.desserts = response.data;
        this.test = false;
      });
  },
  methods: {
    getDTPDF() {
      this.dtpdfload = true;
      axios
        .get("/getDeliveryPDF", {
          params: { dtno: this.DTNO }
        })
        .then(response => {
          this.dtpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getDTEXCEL() {
      this.dtpdfload = true;
      axios
        .get("/getDTExcel", {
          params: { dtno: this.DTNO }
        })
        .then(response => {
          this.dtpdfload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getDOC(item) {
      this.DTNO = item.DT_No
      this.wiresling = item.Wiresling
      this.dialogg = true;
    },
    getWire() {
      window.open(this.wiresling, "_blank");
    }
  }
};
</script>

<style>
</style>