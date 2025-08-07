"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Loader2, Send, Sparkles } from "lucide-react";
import ProtectedLayout from "./layout";

export default function AIQASection() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;

    setIsLoading(true);
    setResponse("");

    try {
      const token = localStorage.getItem("access_token");
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          question,
        }),
      });

      if (!res.ok) {
        throw new Error("Error al generar respuesta");
      }

      const data = await res.json();

      const fullMessage = data.message;

      const thinkMatch = fullMessage.match(/<think>([\s\S]*?)<\/think>/);
      const agentThought = thinkMatch ? thinkMatch[1].trim() : null;

      const userResponse = fullMessage
        .replace(/<think>[\s\S]*?<\/think>/, "")
        .trim();

      console.log("Agente pensó:", agentThought);
      setResponse(userResponse);
    } catch (error) {
      setResponse(
        "Lo siento, ocurrió un error al generar la respuesta. Por favor, inténtalo de nuevo."
      );
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setQuestion("");
    setResponse("");
  };

  return (
    <ProtectedLayout>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4">
        <div className="mx-auto max-w-4xl space-y-6">
          {/* Header */}
          <div className="text-center space-y-2">
            <div className="flex items-center justify-center gap-2">
              <Sparkles className="h-8 w-8 text-blue-600" />
              <h1 className="text-3xl font-bold text-gray-900">AI Assistant</h1>
            </div>
            <p className="text-gray-600">
              Haz cualquier pregunta y obtén respuestas inteligentes al instante
            </p>
          </div>

          <Card className="shadow-lg">
            <CardHeader>
              <CardTitle className="text-lg">¿Qué te gustaría saber?</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-4">
                <Textarea
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  placeholder="Escribe tu pregunta aquí... Por ejemplo: '¿Cómo funciona la inteligencia artificial?' o '¿Cuáles son los beneficios del ejercicio?'"
                  className="min-h-[120px] resize-none"
                  disabled={isLoading}
                />
                <div className="flex gap-2">
                  <Button
                    type="submit"
                    disabled={!question.trim() || isLoading}
                    className="flex-1"
                  >
                    {isLoading ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        Generando respuesta...
                      </>
                    ) : (
                      <>
                        <Send className="mr-2 h-4 w-4" />
                        Enviar pregunta
                      </>
                    )}
                  </Button>
                  {(question || response) && (
                    <Button
                      type="button"
                      variant="outline"
                      onClick={handleClear}
                      disabled={isLoading}
                    >
                      Limpiar
                    </Button>
                  )}
                </div>
              </form>
            </CardContent>
          </Card>

          {/* Response Section */}
          {(response || isLoading) && (
            <Card className="shadow-lg">
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Sparkles className="h-5 w-5 text-blue-600" />
                  Respuesta
                </CardTitle>
              </CardHeader>
              <CardContent>
                {isLoading && !response ? (
                  <div className="flex items-center justify-center py-8">
                    <div className="text-center space-y-2">
                      <Loader2 className="h-8 w-8 animate-spin mx-auto text-blue-600" />
                      <p className="text-gray-600">Generando respuesta...</p>
                    </div>
                  </div>
                ) : (
                  <div className="prose prose-gray max-w-none">
                    <div className="whitespace-pre-wrap text-gray-800 leading-relaxed">
                      {response}
                      {isLoading && (
                        <span className="inline-block w-2 h-5 bg-blue-600 animate-pulse ml-1" />
                      )}
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          )}

          {/* Example Questions */}
          {!response && !isLoading && (
            <Card className="shadow-lg">
              <CardHeader>
                <CardTitle className="text-lg">Preguntas de ejemplo</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid gap-2 sm:grid-cols-2">
                  {[
                    "¿Cómo puedo mejorar mi productividad?",
                    "Explícame qué es el machine learning",
                    "¿Cuáles son las mejores prácticas de programación?",
                    "¿Cómo funciona la criptografía?",
                  ].map((example, index) => (
                    <Button
                      key={index}
                      variant="ghost"
                      className="justify-start h-auto p-3 text-left"
                      onClick={() => setQuestion(example)}
                    >
                      <div className="text-sm text-gray-700">{example}</div>
                    </Button>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </ProtectedLayout>
  );
}
