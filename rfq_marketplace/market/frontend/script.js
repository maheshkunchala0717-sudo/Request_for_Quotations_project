// =========================
// LOGIN INFORMATION
// =========================

const token = localStorage.getItem("token");
const role = localStorage.getItem("role");


// =========================
// CHECK LOGIN
// =========================

if (!token) {

    window.location.href = "/";

}


// =========================
// BUYER ACTION
// =========================

const buyerActions =
    document.getElementById("buyer-actions");


if (role === "buyer") {

    buyerActions.innerHTML = `

        <button
            id="createRfqButton">
            Create RFQ
        </button>

    `;


    document
        .getElementById("createRfqButton")
        .addEventListener("click", function() {

            window.location.href =
                "/create-rfq/";

        });

}


// =========================
// LOAD RFQs
// =========================

async function loadRFQs() {

    try {

        const response =
            await fetch(
                "/rfqs/",
                {
                    method: "GET",

                    headers: {
                        "Authorization":
                            "Token " + token,

                        "Content-Type":
                            "application/json"
                    }
                }
            );


        // Authentication failed
        if (response.status === 401) {

            alert(
                "Your session has expired. Please login again."
            );


            localStorage.removeItem("token");
            localStorage.removeItem("role");


            window.location.href = "/";

            return;

        }


        const data =
            await response.json();


        console.log(
            "RFQ data:",
            data
        );


        const container =
            document.getElementById(
                "rfq-container"
            );


        container.innerHTML = "";


        // No RFQs
        if (
            !Array.isArray(data) ||
            data.length === 0
        ) {

            container.innerHTML =
                "<p>No RFQs available.</p>";

            return;

        }


        // =========================
        // DISPLAY RFQs
        // =========================

        data.forEach(function(rfq) {

            const rfqDiv =
                document.createElement("div");


            rfqDiv.classList.add(
                "rfq-card"
            );


            rfqDiv.innerHTML = `

                <h3>

                    <a href="/rfq-details/?id=${rfq.id}">
                        ${rfq.product_service || "RFQ"}
                    </a>

                </h3>


                <p>
                    <strong>Description:</strong>
                    ${rfq.description || "No description"}
                </p>


                <p>
                    <strong>Quantity:</strong>
                    ${rfq.quantity || "N/A"}
                </p>


                <p>
                    <strong>Deadline:</strong>
                    ${rfq.dead_line || "N/A"}
                </p>

            `;


            container.appendChild(
                rfqDiv
            );

        });

    }


    catch (error) {

        console.error(
            "Error loading RFQs:",
            error
        );


        document.getElementById(
            "rfq-container"
        ).innerHTML =
            "<p>Unable to connect to Django server.</p>";

    }

}


// =========================
// START
// =========================

loadRFQs();