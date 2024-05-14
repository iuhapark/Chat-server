"use client";

import { useForm, SubmitHandler } from "react-hook-form"
import { useState } from "react";

type Inputs = {
  question: string
  exampleRequired?: string
}


export default function Home() {
  const [message, setMessage] = useState('')
  
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = (data) => {
    console.log('input content : '+JSON.stringify(data))
    fetch('http://localhost:8000/titanic', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => setMessage(data.answer))
    .catch((error) => console.log("error:", error));
  }
  console.log(watch("question")) //모니터링, 상태 값이 변하면 찍어줌

  return (
    <>
    <div className="h-[3vh] items-center flex justify-center px-5 lg:px-0"></div>
    <div className="items-center flex justify-center dark:text-white text-[28px]">GPT</div>
      <div className="h-[80vh] items-center flex justify-center px-5 lg:px-0">
        <div className="flex flex-col items-center justify-center w-full text-2xl xl:text-4xl font-extrabold text-900">
          <h1> How can I help you today? </h1>
        </div></div>
        <div className="mx-auto max-w-[100vh] flex flex-col gap-4">
          <h4>{message? message:""}</h4>
          <form onSubmit={handleSubmit(onSubmit)}>
          <input
          type="text"
          {...register("question", { required: true })} 
            className="w-full px-5 py-3 rounded-lg font-medium text-black bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            placeholder="Message here"
          />
          <div className="h-[5vh] py-3 items-center justify-center">
          <button type="submit"
          className="h-[5vh] w-[15vh] relative  p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-pink-500 to-orange-400 group-hover:from-pink-500 group-hover:to-orange-400 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800">
            Send
          </button>
          <button type="submit"
          className="h-[5vh] w-[15vh] relative p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-pink-500 to-orange-400 group-hover:from-pink-500 group-hover:to-orange-400 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800">
            Titanic
          </button></div>
          </form>
          {errors.question && <span>This field is required</span>}
        </div>
    </>
  );
}
