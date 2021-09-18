import React, { useState } from "react";
import { Input, IconButton, Heading, Grid, GridItem } from "@chakra-ui/react";
import { SearchIcon, CloseIcon } from "@chakra-ui/icons";

const InputBox = ({ retrieveInfo }) => {
  const [value, setValue] = useState("");

  const handleSearch = () => {
    //search handler
    if (value.trim() !== "" || value !== null) {
      retrieveInfo(value);
    }
  }

  const handleSearchChange = (e) => {
    if (e.key === "Enter") {
      handleSearch();
    } else {
      setValue(e.target.value);
    }
  }

  return (
    <div>
      <Grid
        templateRows="repeat(2, 1fr)"
        templateColumns="repeat(5, 1fr)"
        gap={1}
      >
        <GridItem colSpan={5}>
          <Heading as="h1" size="lg" color="#2D3748">
            What do Canadian political parties think about...
          </Heading>
        </GridItem>
        <GridItem colSpan={3}>
          <Input
            value={value}
            onChange={(e) => handleSearchChange(e)}
            placeholder='Input topic here (ex: "the environment")'
            borderRadius="200"
            size="lg"
            bgColor="white"
            boxShadow="base"
          />
        </GridItem>
        <GridItem colSpan={1}>
          <IconButton
            onClick={() => setValue("")}
            borderRadius="200"
            colorScheme="red"
            size="lg"
            aria-label="Search Topic"
            icon={<CloseIcon />}
            boxShadow="base"
          />
          &nbsp;
          <IconButton
            onClick={() => handleSearch()}
            borderRadius="200"
            colorScheme="blue"
            size="lg"
            aria-label="Search Topic"
            icon={<SearchIcon />}
            boxShadow="base"
          />
        </GridItem>
      </Grid>
      <br />
    </div>
  );
};

export default InputBox;
