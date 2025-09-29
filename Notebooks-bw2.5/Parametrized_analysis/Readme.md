# Uncertainty and Sensitivity Analysis on Parameterized Inventories

The notebook provided in this section enables you to perform **uncertainty and sensitivity analysis** on parameterized inventories.  

In practice, this means that some of the flows in the inventory are expressed as **formulas defined in terms of parameters**.  
For example, the amount of heat required can be modeled as a function of the heat efficiency of the machinery employed.

---

## Example: ALIGNED Dummy Case (Biobased Product)

In the ALIGNED dummy case of a biobased product, several flows have been parameterized in terms of general **material** and **technological** properties.  
Examples include:

- Water content  
- Reactor efficiency  

This approach allows us to flexibly model changes in system behavior by adjusting key parameters that might also affect multiple flows at the same time.

---

## How to Parameterize Your LCI

To parameterize your Life Cycle Inventory (LCI), you need to add **two additional fields** to the CSV file describing your system:

1. **`formula`**  
   Provides the expression to calculate an exchange in terms of parameters.  

2. **`group`**  
   Used to identify which group the parameters belong to.  

For the purposes of this tutorial, we simplify by assigning **all parameters to the same group**.  
For a deeper understanding of groups and parameters, refer to the Brightway guide:  
👉 [Brightway Documentation](https://github.com/brightway-lca/brightway2/blob/master/docs/intro.rst)


### Defining Parameters and Uncertainty

Parameters, along with their uncertainty information, are defined in a separate CSV file.  
An example is provided in:  

**`ALIGNED-LCI-biobased-product-parameters-dummy.csv`**

Here you can define the parameter characteristics including their uncertainty information. Always include the database name to which the parameters belong.

---

## Workflow

Once you have defined your parameters in a singel CSV and incorporated formulas into the foreground system,  you can proceed by following the **provided tutorial notebook**.

---

### Author  
Rebecca Belfiore, INSAT 2025