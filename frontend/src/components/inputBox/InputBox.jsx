import React from "react";
import { Input, IconButton } from "@chakra-ui/react";
import { SearchIcon } from "@chakra-ui/icons";

const InputBox = () => {
  return (
    <div>
      <Input placeholder='Input topic here (ex: "Environment")' size="lg" />
      <IconButton aria-label="Search Topic" icon={<SearchIcon />} />
    </div>
  );
};

export default InputBox;
