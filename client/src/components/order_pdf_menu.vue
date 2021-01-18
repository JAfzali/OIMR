<template>
    <v-dialog v-model="dialog" width="350">
      <v-card>
        <v-list-item two-line class="light-blue lighten-4">
          <v-list-item-content>
            <v-list-item-title class="headline"></v-list-item-title>
            <v-list-item-subtitle>Order Numbers</v-list-item-subtitle>
            <v-list-item-title class="headline">{{
                currentOrdernr
              }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <div :class="padding_class">
          <v-btn
            :loading="recpdfload"
            depressed
            color="white"
            block
            @click="getReceivedPDF"
          >
            Receive
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="orderpdfload"
            depressed
            color="white"
            block
            @click="getOrderPDF"
          >
            Order Confirmation
            <v-spacer/>
          </v-btn>
          <v-btn depressed color="white" block @click="getCOC_MC">
            COC Machining
            <v-spacer/>
          </v-btn>
          <v-btn depressed color="white" block @click="getCOC_HB">
            COC Hardbanding
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="preinvpdfload"
            depressed
            color="white"
            block
            @click="getPreinvPDF"
          >
            Pre Invoice
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="inspreploadPDF"
            depressed
            color="white"
            block
            @click="getInspectionTypePDF"
          >
            Inspection Report PDF
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="inspreploadEXCEL"
            depressed
            color="white"
            block
            @click="getInspectionTypeEXCEL"
          >
            Inspection Report EXCEL
            <v-spacer/>
          </v-btn>
        </div>
      </v-card>
    </v-dialog>
</template>

<script>
import axios from 'axios'

export default {
  name: 'pdf_menu',
  props: ['currentOrdernr', 'currentrec', 'currentCOCHB', 'currentCOCMC', 'eq', 'dialog'],
  data() {
    return {
      preinvpdfload: false,
      recpdfload: false,
      orderpdfload: false,
      inspreploadPDF: false,
      inspreploadEXCEL: false,
      padding_class: 'pl-2'
    }
  },
  watch: {
    dialog(value) {
      console.log(value)
    }
  },
  methods: {
    getInspectionTypePDF() {
      this.inspreploadPDF = true
      if (this.eq === "Drill Pipe") {
        this.getdpPDF()
      } else if (this.eq === "Heavy Weight") {
        this.gethwPDF()
      } else if (this.eq === "Drill Collar") {
        this.getdcPDF()
      }
    },
    getInspectionTypeEXCEL() {
      this.inspreploadEXCEL = true
      if (this.eq === "Drill Pipe") {
        this.getExceldp()
      } else if (this.eq === "Heavy Weight") {
        this.getExcelhw()
      } else if (this.eq === "Drill Collar") {
        this.getExceldc()
      }
    },
    getReceivedPDF() {
      this.recpdfload = true;
      axios
        .get("/getReceivedPDF", {
          params: { receivednr: this.currentrec }
        })
        .then(response => {
          this.recpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getOrderPDF() {
      this.orderpdfload = true;
      axios
        .get("/getOrderPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.orderpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getCOC_HB() {
      window.open(this.currentCOCHB, "_blank");
    },
    getCOC_MC() {
      window.open(this.currentCOCMC, "_blank");
    },
    getPreinvPDF() {
      this.preinvpdfload = true;
      axios
        .get("/getPreinvPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.preinvpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getdpPDF() {
      console.log(this.currentOrdernr);
      axios
        .get("/getdpPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.inspreploadPDF = false
          window.open(response.data.pdflink, "_blank");
        });
    },
    gethwPDF() {
      axios
        .get("/gethwPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.inspreploadPDF = false
          window.open(response.data.pdflink, "_blank");
        });
    },
    getdcPDF() {
      axios
        .get("/getdcPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.inspreploadPDF = false
          window.open(response.data.pdflink, "_blank");
        });
    },
    getExceldp() {
      axios
        .get("/getdpExcel", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.inspreploadEXCEL = false
          window.open(response.data.excellink, "_blank");
        });
    },
    getExcelhw() {
      axios
        .get("/gethwExcel", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.inspreploadEXCEL = false
          window.open(response.data.excellink, "_blank");
        });
    },
    getExceldc() {
      axios
        .get("/getdcExcel", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.inspreploadEXCEL = false
          window.open(response.data.excellink, "_blank");
        });
    },
  }
}
</script>

<style scoped>

</style>
